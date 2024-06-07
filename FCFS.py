# Python program for FCFS disk scheduling algorithm


def FCFS(arr, head, size):

    seek_count = 0;
    distance, cur_track = 0, 0;

    for i in range(size):
        cur_track = arr[i];

		# calculate absolute distance
        distance = abs(cur_track - head);

		# increase the total count
        seek_count += distance;

		# accessed track is now new head
        head = cur_track;
	
    average = seek_count / size;
    
    print("Total number of seek tracks = ", seek_count) 

	# Seek sequence would be the same
	# as request array sequence
    print("Seek Sequence : ");

    for i in range(size):
        print(arr[i]);
     
    # calculate the average
    print("Average number of tracks travelled = ", average)
    
    
# Driver code
if __name__ == '__main__':
    
    # to get the initial head position
    head=int(input("Initial head position: "))
    
    # to get the size of the array
    size= int(input("Number of pathes: "))
    
	# request array
    print("Sequence: ")
    arr= []
    for i in range(size):
        arr.append(int(input()))
    
    FCFS(arr, head, size)
        
	

