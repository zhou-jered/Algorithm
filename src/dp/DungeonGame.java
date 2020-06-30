package dp;

import java.util.Arrays;

public class DungeonGame {

    public static int calculateMinimumHP(int[][] dungeon) {
        int n = dungeon.length;
        int m = dungeon[0].length;
        int[][] maxRemain = new int[n][m];
        for (int i = 0; i < n; i++) {
            Arrays.fill(maxRemain[i], Integer.MAX_VALUE);
        }

        int result = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if(i<n-1) {

                }
            }
        }

        Arrays.stream(dungeon).map(v -> Arrays.toString(v)).forEach(System.out::println);
        System.out.println("-------");
        Arrays.stream(maxRemain).map(v -> Arrays.toString(v)).forEach(System.out::println);
        return maxRemain[0][0] > 0 ? maxRemain[0][0] : 0;
    }

    public static void main(String[] args) {
        int[][] dungon = new int[][]{{-2, -3, 3}, {-5, -10, 1}, {10, 30, -5}};
        System.out.println(calculateMinimumHP(dungon));
    }

}
