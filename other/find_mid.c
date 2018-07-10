#include <stdio.h>

#define MIN(a, b) (a)<=(b)?(a):(b)

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
    int *start1 = nums1;
    int *start2 = nums2;
    int *mid1 = NULL;
    int *mid2 = NULL;
    int len1 = 0;
    int len2 = 0;
	int *low_mid = NULL;
	int *high_mid = NULL;
	
	int *end1 = nums1 + (nums1Size - 1);
	int *end2 = nums2 + (nums2Size - 1);
   
    int left = (nums1Size + nums2Size)/2;
    if ((nums1Size + nums2Size)%2 == 0){
        left --;
    }
    
    if (nums1 == NULL && nums2 == NULL) {
        return -1;
    }
	
	while (left > 0){
        if (start1 > end1) {
            start2 += left;
            left = 0;
            break;
        }

        if (start2 > end2) {
            start1 += left;
            left = 0;
            break;
        }
		
        mid1 = MIN(start1 + (left-1)/2, end1);
        mid2 = MIN(start2 + (left-1)/2, end2);
		
		len1 = mid1 - start1 + 1;
		len2 = mid2 - start2 + 1;
		
		if (*mid1 == *mid2){
			if ((len1+len2) <= left){
				start1 = mid1 + 1;
				start2 = mid2 + 1;
				left = left - (len1 + len2);
			} else if ((len1 + len2) > left){
				if (mid1 == end1){
					start1 = end1 + 1;
					start2 = mid2;
				} else if (mid2 == end2){
					start2 = end2+1;
					start1 = mid1;
				} else if (*(mid1+1) <= *(mid2+1)){
					start1 = mid1 + 1;
					start2 = mid2;
				} else {
					start2 = mid2 + 1;
					start1 = mid1;
				}
				left = 0;
			}
		} else if (*mid1 < *mid2) {
			start1 = mid1 + 1;
			left -= len1;
		} else {
			start2 = mid2 + 1;
			left -= len2;
		}
	}
	
	if((nums1Size + nums2Size) %2 == 1){
        if (start1 > end1){
            return *start2;
        } else if (start2 > end2){
            return *start1;
        }else if (*start1 <= *start2){
            return *start1;
        } else {
            return *start2;
        }
	} else {
        if (start1 > end1){
            return (double)(*start2 +*(start2+1))/2;
        }
        else if (start2 > end2){
            return (double)(*start1 + *(start1+1))/2;
        } else {
			if (*start1 <= *start2){
				low_mid = start1;
				if ((start1 < end1) && (*(start1+1) <= *start2)){
					high_mid = start1+1;
				} else {
					high_mid = start2;
				}
			} else {
				low_mid = start2;
				if ((start2 < end2) && (*(start2+1) <= *start1)){
					high_mid = start2 + 1;
				} else {
					high_mid = start1;
				}
			}
            return (double)(*low_mid+*high_mid)/2;
        }
	}
	
}


int main(){
	int l1[10] = {1, 2};
	int l2[10] = {1, 2};
	
	double val = 0;
	
	val = findMedianSortedArrays((int *)l1, 2, (int *)l2, 2);
	printf("Mid is %f!\n", val);
}