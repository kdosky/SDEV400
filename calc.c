#include <stdio.h>
int main() {
    char operator;
    double first, second;
    printf("\nSelect from the meue:\n\n");
    printf("  1 - Addittion\n");
    printf("  2 - Subtraction\n");
    printf("  3 - Multiplication\n");
    printf("  4 - Division\n\n");
    printf("What is your selection: ");
    scanf("%c", &operator);
    printf("\nEnter your first digit: ");
    scanf("%lf", &first);
    printf("Enter your second digit: ");
    scanf("%lf", &second);


    switch (operator) {
    case '1':
    	printf("\nResults: ");
        printf("%.1lf + %.1lf = %.1lf", first, second, first + second);
        break;
    case '2':
    	printf("\nResults: ");
        printf("%.1lf - %.1lf = %.1lf", first, second, first - second);
        break;
    case '3':
    	printf("\nResults: ");
        printf("%.1lf * %.1lf = %.1lf", first, second, first * second);
        break;
    case '4':
    	printf("\nResults: ");
        printf("%.1lf / %.1lf = %.1lf", first, second, first / second);
        break;
        // operator doesn't match any case constant
    default:
        printf("Error! operator is not correct");
    }

    return 0;
}