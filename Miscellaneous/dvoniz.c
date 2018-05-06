int main(void) {
	int N, S, i, o, left, right;
	scanf("%d %d", &N, &S);
	for (i = 0; i < N; i++) {
		scanf("%d", &a[i]);
	}
	o = 0; left = 0; right = 0;
	for (i = 0; i < N; i++) {
		while(i+o+1 < N) {
			// puts("grab two more.");
			left += a[i+o/2];
			right -= a[i+o/2];
			right += a[i+o];
			right += a[i+o+1];
			// printf("l: %d;  r: %d\n", left, right);
			if (left + right > 2*S) {
				// puts("too big; roll it back!");
				left -= a[i+o/2];
				right += a[i+o/2];
				right -= a[i+o];
				right -= a[i+o+1];
				// printf("l: %d;  r: %d\n", left, right);
				break;
			}
			o += 2;
		}
		// puts("move back until both left and right are ok.");
		while (left > S || right > S) {
			o -= 2;
			left -= a[i+o/2];
			right += a[i+o/2];
			right -= a[i+o];
			right -= a[i+o+1];
			// printf("l: %d;  r: %d\n", left, right);
		}

		if (o > 0) {
			// puts("step in the left and right sides.");
			left -= a[i];
			right -= a[i+o-1];
			// printf("l: %d;  r: %d\n", left, right);
		}
		a[i] = o;
		o = (o > 0) ? o-2 : 0;
		printf("%d\n", a[i]);
	}

	return 0;
}