// Problem Statement #

// We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

// Write a function to sort the objects in-place on their creation sequence number in O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

const cyclic_sort = function (nums) {
  for(i=0;i<nums.length;i++){
     pos=i;
     curritem=nums[i];
     counter=i+1;
     while(counter<nums.length){
       if(curritem>nums[counter]) pos++;
       counter++;
     }
     if(pos!=i){
        [nums[pos], curritem] = [curritem, nums[pos]];
        while(pos!=i){
         pos=i;
         counter=i+1;
         while(counter<nums.length){
          if(curritem>nums[counter]) pos++;
           counter++;
         }
         [nums[pos], curritem] = [curritem, nums[pos]];
        }
     }
  }
  return nums;
};

console.log(`${cyclic_sort([3, 1, 5, 4, 2])}`);
console.log(`${cyclic_sort([2, 6, 4, 3, 1, 5])}`);
console.log(`${cyclic_sort([1, 5, 6, 4, 3, 2])}`);