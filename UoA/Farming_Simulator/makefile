# Source file sections
main-text: main.cpp
	@g++ main.cpp Farm.cpp Land.cpp oopGame.cpp Produce.cpp Crops.cpp -o main1
	@./main1


main-graphics: main.cpp
	@g++ main.cpp Farm.cpp Land.cpp oopGame.cpp Produce.cpp Crops.cpp -lsfml-graphics -lsfml-window -lsfml-system -lsfml-audio -o main2
	@./main2


# Test files
test-crops: main.cpp
	@g++ main.cpp Crops.cpp Produce.cpp -o testCrops
	@./testCrops


# Clean source files
clean-1: # test-based
	@rm -rf main1

clean-2: # graphic-based
	@rm -rf main2

# Clean test files
clean-t-crops:
	@rm -rf testCrops