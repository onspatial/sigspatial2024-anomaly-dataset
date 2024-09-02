process_1=true
process_2=true
while $process_1 || $process_2; do
    if $process_1; then
        start_time_1=$(date +%s)
        /bin/python /home/amiri/Research/outlier-dev/src/main/python/process.py city_centralized_1
        end_time_1=$(date +%s)
        process_time_1=$((end_time_1 - start_time_1))
        echo "Process Time: $process_time_1"
        if [ $process_time_1 -lt 10 ]; then
            process_1=false
        fi
        continue
    fi

    if $process_2; then
        start_time_2=$(date +%s)
        /bin/python /home/amiri/Research/outlier-dev/src/main/python/process.py city_infectious_1,city_location_1 84
        end_time_2=$(date +%s)
        process_time_2=$((end_time_2 - start_time_2))
        echo "Process Time: $process_time_2"
        if [ $process_time_2 -lt 10 ]; then
            process_2=false
        fi
        continue
    fi

done

echo "All processes are done! at $(date)"
