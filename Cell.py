import Main
import RPIO.GPIO as GPIO


class Cell:

    def __init__(self, cell, data_pin):
        self.cell = cell
        self.pin = data_pin
        self.cur_let = Main.letter_que.index(self.cell)
        RPIO.setup(self.pin, RPIO.OUT)

    def shift_out_e(self):
        pass

    def shift_out_E(self):
        pass

    def shift_out_t(self):
        pass

    def shift_out_T(self):
        pass

    def shift_out_a(self):
        pass

    def shift_out_A(self):
        pass

    def shift_out_o(self):
        pass

    def shift_out_O(self):
        pass

    def shift_out_i(self):
        pass

    def shift_out_I(self):
        pass

    def shift_out_n(self):
        pass

    def shift_out_N(self):
        pass

    def shift_out_s(self):
        pass

    def shift_out_S(self):
        pass

    def shift_out_r(self):
        pass

    def shift_out_R(self):
        pass

    def shift_out_h(self):
        pass

    def shift_out_H(self):
        pass

    def shift_out_d(self):
        pass

    def shift_out_D(self):
        pass

    def shift_out_l(self):
        pass

    def shift_out_L(self):
        pass

    def shift_out_u(self):
        pass

    def shift_out_U(self):
        pass

    def shift_out_c(self):
        pass

    def shift_out_C(self):
        pass

    def shift_out_m(self):
        pass

    def shift_out_M(self):
        pass

    def shift_out_f(self):
        pass

    def shift_out_F(self):
        pass

    def shift_out_y(self):
        pass

    def shift_out_Y(self):
        pass

    def shift_out_w(self):
        pass

    def shift_out_W(self):
        pass

    def shift_out_g(self):
        pass

    def shift_out_G(self):
        pass

    def shift_out_p(self):
        pass

    def shift_out_P(self):
        pass

    def shift_out_b(self):
        pass

    def shift_out_B(self):
        pass

    def shift_out_v(self):
        pass

    def shift_out_V(self):
        pass

    def shift_out_k(self):
        pass

    def shift_out_K(self):
        pass

    def shift_out_x(self):
        pass

    def shift_out_X(self):
        pass

    def shift_out_q(self):
        pass

    def shift_out_Q(self):
        pass

    def shift_out_j(self):
        pass

    def shift_out_J(self):
        pass

    def shift_out_z(self):
        pass

    def shift_out_Z(self):
        pass

    def shift_out_dot(self):
        pass

    def shift_out_space(self):
        pass

    # dispatch table for letter writing methods
    letter_map = {'e': shift_out_e, 'E': shift_out_E, 't': shift_out_t, 'T': shift_out_T,
                  'a': shift_out_a, 'A': shift_out_A, 'o': shift_out_o, 'O': shift_out_O,
                  'i': shift_out_i, 'I': shift_out_I, 'n': shift_out_n, 'N': shift_out_N,
                  's': shift_out_s, 'S': shift_out_S, 'r': shift_out_r, 'R': shift_out_R,
                  'h': shift_out_h, 'H': shift_out_H, 'd': shift_out_d, 'D': shift_out_D,
                  'l': shift_out_l, 'L': shift_out_L, 'u': shift_out_u, 'U': shift_out_U,
                  'c': shift_out_c, 'C': shift_out_C, 'm': shift_out_m, 'M': shift_out_M,
                  'f': shift_out_f, 'F': shift_out_F, 'y': shift_out_y, 'Y': shift_out_Y,
                  'w': shift_out_w, 'W': shift_out_W, 'g': shift_out_g, 'G': shift_out_G,
                  'p': shift_out_p, 'P': shift_out_P, 'b': shift_out_b, 'B': shift_out_B,
                  'v': shift_out_v, 'V': shift_out_V, 'k': shift_out_k, 'K': shift_out_K,
                  'x': shift_out_x, 'X': shift_out_X, 'q': shift_out_q, 'Q': shift_out_Q,
                  'j': shift_out_j, 'J': shift_out_J, 'z': shift_out_z, 'Z': shift_out_Z,
                  '.': shift_out_dot, ' ': shift_out_space}
