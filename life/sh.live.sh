cd ..
 sh sh.mvn.sh
cd life
java -Dlog4j2.configurationFactory=pol.log.CustomConfigurationFactory -Dlog.rootDirectory=logs -Dsimulation.test=c02 -jar ../jar/pol.jar -configuration modified.properties -until 20160
