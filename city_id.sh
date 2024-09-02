cd /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_hunger_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_hunger_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev

cd /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_work_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_work_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev

cd /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_social_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_social_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev

cd /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_interest_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_interest_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev

cd /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_combined_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/atl_1000_combined_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev
echo waiting for 5 to finish
wait

cd /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_hunger_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_hunger_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev

cd /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_work_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_work_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev

cd /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_social_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_social_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev

cd /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_interest_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_interest_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev

cd /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_combined_outliers
echo "Processing /home/amiri/Research/outlier-dev/city_centralized_test/brln_1000_combined_outliers"
touch run.lock
bash run.sh >run.log.txt 2>&1 && touch run.unlock & 
cd /home/amiri/Research/outlier-dev
echo waiting for 5 to finish
wait

wait
# shutdown -h now
