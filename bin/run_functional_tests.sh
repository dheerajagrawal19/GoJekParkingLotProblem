#cd ..
echo "Testing of Custom use cases Start"
python -m functional_spec.test.TestParkingLot
echo "Testing of Custom use cases End"
curr_dir="`pwd`"
test_file_path="$curr_dir/functional_spec/test/input_file.txt"
echo "Testing via File Input Start"
python -m functional_spec.src.ParkingLotMain $test_file_path
echo "Testing via File Input End"