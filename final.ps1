
$CONTAINER_NAME="test1"
$OUTPUT_DIRECTORY=".\\service-result"


New-Item -Path $OUTPUT_DIRECTORY -ItemType Directory -Force


docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/res_dpre.csv $OUTPUT_DIRECTORY\res_dpre.csv
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-1.txt $OUTPUT_DIRECTORY\eda-in-1.txt
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-2.txt $OUTPUT_DIRECTORY\eda-in-2.txt
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/eda-in-3.txt $OUTPUT_DIRECTORY\eda-in-3.txt
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/vis.png $OUTPUT_DIRECTORY\vis.png
docker cp ${CONTAINER_NAME}:/home/doc-bd-a1/k.txt $OUTPUT_DIRECTORY\k.txt


# Stop the container
docker stop $CONTAINER_NAME

Write-Host "Output files copied and container stopped."
