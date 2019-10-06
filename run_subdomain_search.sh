#!/bin/bash
script_dir=$(pwd)
START=$(date +%s)
filename="list_of_domains.txt"
while IFS= read -r line || [ -n "$line" ]; do
    # cleari new subdomains ära alati enne algust:
    # run subdomain enumeration tools and save results to a txt file
    echo "searching for subdomains for: ${line}"
    echo "using amass:"
    #amass enum -o "results/amass_${line}.txt" -d $line
    echo "using sublist3r:"
    cd tools/Sublist3r/
    python3 sublist3r.py -d $line -o "../../results/sublist3r_${line}.txt"
    cd ../
    echo "using findomain:"
    ./findomain-linux -t $line -u ../results/findomain_${line}.txt
    cd $script_dir
    cd results/
    echo "aggregate results to one file"
    # aggregate all unique results to a new file
    sort -u amass_${line}.txt sublist3r_${line}.txt findomain_${line}.txt > result_${line}.txt
    # check if domain has a known subdomains list to compare to
    # if it has, compare, if not, create it
    cd $script_dir
    FILE=known_subdomains/${line}.txt
    if [ -f "$FILE" ]; then
        echo "comparing known_subdomains/${line}.txt to results/result_${line}.txt"
        grep -Fvxf known_subdomains/${line}.txt results/result_${line}.txt | grep . > new_subdomains/new_${line}.txt
        # 
        cat new_subdomains/new_${line}.txt >> known_subdomains/${line}.txt
    else 
        echo "$FILE does not exist, creating ..."
        mv results/result_${line}.txt results/${line}.txt
        mv results/${line}.txt known_subdomains/
        echo "created base comparison file known_subdomains/${line}.txt for next run"
    fi
    cd $script_dir
done < $filename
END=$(date +%s)
DIFF=$(( $END - $START ))
seconds=$(($DIFF % 60))
minutes=$(($DIFF / 60))
echo "It took $minutes minutes and $seconds seconds"