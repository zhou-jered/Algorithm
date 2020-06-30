package tk;

import java.util.Arrays;

/**
 * 找到数组中没出现的最小正数
 * 好像有次面试问到过这个题,
 * 思路还是比较有趣的，遇到正数n，如果这个正数 < 数组长度，就更新数组第n个数字为n。
 * 遍历一边之后，如果有未更新的位置就是那个没出现的数字。
 */
public class FirstMissingPositive {
    public static int firstMissingPositive(int[] nums) {
        int[] other = new int[nums.length + 1];
        for(int i =0;i<nums.length;i++) {
            other[i] = -1;
        }
        for(int i =0;i<nums.length;i++) {
            int n = nums[i];
            if(n>0 && n<=nums.length) {
                other[n] = n;
            }
        }
        System.out.println(Arrays.toString(other));
        for(int i =1;i<other.length;i++) {
            if(other[i]<1) {
                return i;
            }
        }
        return other.length;
    }

    public static void main(String[] args) {
        int[] a = new int[]{10,1,2};
        System.out.println(firstMissingPositive(a));
    }

}
