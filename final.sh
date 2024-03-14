CONTAINER_NAME="test1"
OUTPUT_DIRECTORY="./service-result"

mkdir -p $OUTPUT_DIRECTORY

docker cp $CONTAINER_NAME:/home/doc-bd-a1/dpre_output.csv $OUTPUT_DIRECTORY/dpre_output.csv
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-1.txt $OUTPUT_DIRECTORY/eda-in-1.txt
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-2.txt $OUTPUT_DIRECTORY/eda-in-2.txt
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-3.txt $OUTPUT_DIRECTORY/eda-in-3.txt
docker cp $CONTAINER_NAME:/home/doc-bd-a1/vis.png $OUTPUT_DIRECTORY/vis.png
docker cp $CONTAINER_NAME:/home/doc-bd-a1/k.txt $OUTPUT_DIRECTORY/k.txt

docker stop $CONTAINER_NAME

echo "Output files copied and container stopped."
