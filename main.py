import numpy as np

def lin_reg(x_val, y_val, delta_x=0, delta_y=0):
    x_val = np.array(x_val)
    y_val = np.array(y_val)
    N = x_val.size
    sum_x = np.sum(x_val)
    sum_y = np.sum(y_val)
    sum_x2 = np.sum(x_val ** 2)
    sum_xy = np.sum(x_val * y_val)
    Delta = N * sum_x2 - sum_x ** 2
    A = (sum_x2 * sum_y - sum_x * sum_xy) / Delta
    B = (N * sum_xy - sum_x * sum_y) / Delta
    sigma_y = np.sqrt(np.sum((y_val - A * np.ones(N) - B * x_val) ** 2) / (N-2) + delta_y ** 2 + (B * delta_x) ** 2)
    sigma_A = sigma_y * np.sqrt(sum_x2 / Delta)
    sigma_B = sigma_y * np.sqrt(N /Delta)
    return A, B, sigma_A, sigma_B

def main():
    x = [1, 2, 3]
    y = [3, 4, 4]
    print(lin_reg(x, y))

if __name__ == '__main__':
    main()