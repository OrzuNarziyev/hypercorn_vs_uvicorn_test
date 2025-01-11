start=$(date +%s)
for i in {1..1000}
do
  curl -I --http2  https://localhost:8443/ --insecure
done
end=$(date +%s)
echo "Total Time Taken: $((end - start)) seconds"
