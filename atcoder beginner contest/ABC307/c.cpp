#include <iostream>
#include <deque>
#include <vector>

using namespace std;

int main() {
    int h_a, w_a, h_b, w_b, h_x, w_x;
    cin >> h_a >> w_a;

    deque<string> a(h_a);
    for (int i = 0; i < h_a; i++) {
        cin >> a[i];
    }

    cin >> h_b >> w_b;

    deque<string> b(h_b);
    for (int i = 0; i < h_b; i++) {
        cin >> b[i];
    }

    cin >> h_x >> w_x;

    deque<string> x(h_x);
    for (int i = 0; i < h_x; i++) {
        cin >> x[i];
    }

    vector<vector<char>> c(30, vector<char>(30, '.'));

    for (int pl = 0; pl < 160000; pl++) {
        int a_pl = pl / 400;
        int b_pl = pl % 400;
        for (int i = 0; i < 100; i++) {
            int div = i / 10;
            int mod = i % 10;
            if (mod % 10 < h_a && div < w_a) {
                c[a_pl % 20 + mod][a_pl / 20 + div] = a[mod][div];
            }
            if (mod < h_b && div < w_b) {
                if (b[mod][div] == '#') {
                    c[b_pl % 20 + mod][b_pl / 20 + div] = b[mod][div];
                }
            }
        }
        int cnt = 0;
        for (int i = 0; i < h_x * w_x; i++) {
            if (c[10 + i % h_x][10 + i / h_x] == x[i % h_x][i / h_x]) {
                cnt++;
            }
        }
        if (cnt == h_x * w_x) {
            cout << "Yes" << endl;
            return 0;
        }
        c = vector<vector<char>>(30, vector<char>(30, '.'));
    }

    cout << "No" << endl;

    return 0;
}