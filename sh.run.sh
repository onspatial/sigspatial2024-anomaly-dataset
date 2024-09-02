id=$1
build=$2
agents=1000
while true; do
    if [ "$build" == "build" ]; then
        bash sh.mvn.sh
    fi
    mv exp1/logs exp1/logs_$id_$agents_$(date +%s)

    cd exp1
    echo $(date)

    echo "numOfAgents = $agents
numOfAgentInterests =100
numPubsPer1000=10
initialManipulationFilePath = manipulations/pub_outliers.json
seed = 1
maps = maps/atl/map" >modified.properties
    mkdir -p evaluation/$id
    bash sh.live.sh | tee evaluation/$id/life_$agents.log 2>&1
    echo $(date)
    cd ..
    echo "sleeping 10 seconds"
    # agents=$((agents + 1))
    sleep 10
    if [ $? -eq 130 ]; then
        continue
    fi

done
