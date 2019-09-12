import Main
import RPIO.GPIO as GPIO


class Cell:

    def __init__(self, cell, data_pin):
        self.cell = cell
        self.pin = data_pin
        self.cur_let = Main.letter_que.index(self.cell)
        RPIO.setup(self.pin, RPIO.OUT)

    # Retrieve current letter at que index
    def new_let(self):
        self.cur_let = Main.letter_que.index(self.cell)

    # Shift out methods for all letters displayable
    # All same structure, each one simply references
    # a different output schema from letter map
    def shift_out_e(self):
        RPIO.output(self.pin, self.e_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_E(self):
        RPIO.output(self.pin, self.E_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_t(self):
        RPIO.output(self.pin, self.t_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_T(self):
        RPIO.output(self.pin, self.T_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_a(self):
        RPIO.output(self.pin, self.a_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_A(self):
        RPIO.output(self.pin, self.A_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_o(self):
        RPIO.output(self.pin, self.o_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_O(self):
        RPIO.output(self.pin, self.O_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_i(self):
        RPIO.output(self.pin, self.i_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_I(self):
        RPIO.output(self.pin, self.I_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_n(self):
        RPIO.output(self.pin, self.n_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_N(self):
        RPIO.output(self.pin, self.N_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_s(self):
        RPIO.output(self.pin, self.s_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_S(self):
        RPIO.output(self.pin, self.S_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_r(self):
        RPIO.output(self.pin, self.r_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_R(self):
        RPIO.output(self.pin, self.R_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_h(self):
        RPIO.output(self.pin, self.h_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_H(self):
        RPIO.output(self.pin, self.H_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_d(self):
        RPIO.output(self.pin, self.d_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_D(self):
        RPIO.output(self.pin, self.D_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_l(self):
        RPIO.output(self.pin, self.l_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_L(self):
        RPIO.output(self.pin, self.L_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_u(self):
        RPIO.output(self.pin, self.u_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_U(self):
        RPIO.output(self.pin, self.U_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_c(self):
        RPIO.output(self.pin, self.c_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_C(self):
        RPIO.output(self.pin, self.C_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_m(self):
        RPIO.output(self.pin, self.m_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_M(self):
        RPIO.output(self.pin, self.M_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_f(self):
        RPIO.output(self.pin, self.f_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_F(self):
        RPIO.output(self.pin, self.F_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_y(self):
        RPIO.output(self.pin, self.y_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_Y(self):
        RPIO.output(self.pin, self.Y_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_w(self):
        RPIO.output(self.pin, self.w_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_W(self):
        RPIO.output(self.pin, self.W_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_g(self):
        RPIO.output(self.pin, self.g_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_G(self):
        RPIO.output(self.pin, self.G_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_p(self):
        RPIO.output(self.pin, self.p_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_P(self):
        RPIO.output(self.pin, self.P_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_b(self):
        RPIO.output(self.pin, self.b_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_B(self):
        RPIO.output(self.pin, self.B_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_v(self):
        RPIO.output(self.pin, self.v_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_V(self):
        RPIO.output(self.pin, self.V_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_k(self):
        RPIO.output(self.pin, self.k_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_K(self):
        RPIO.output(self.pin, self.K_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_x(self):
        RPIO.output(self.pin, self.x_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_X(self):
        RPIO.output(self.pin, self.X_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_q(self):
        RPIO.output(self.pin, self.q_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_Q(self):
        RPIO.output(self.pin, self.Q_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_j(self):
        RPIO.output(self.pin, self.j_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_J(self):
        RPIO.output(self.pin, self.J_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_z(self):
        RPIO.output(self.pin, self.z_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_Z(self):
        RPIO.output(self.pin, self.Z_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

    def shift_out_dot(self):
        RPIO.output(self.pin, self.dot_map[GPIO_Handler.cur_col()][GPIO_Handler.get_row()])

    def shift_out_space(self):
        RPIO.output(self.pin, self.space_map[GPIO_Handler.get_col()][GPIO_Handler.get_row()])

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

    # Writing diagrams
    # Inverted each sequence 8 long, only first 5 bits encoding
    # last 3 tied to col in call, should be common on list columns
    e_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    E_map = [[1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    t_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    T_map = [[0, 0, 1, 0, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    a_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    A_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    o_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    O_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    i_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    I_map = [[0, 0, 1, 0, 0, 1, 0, 0], [1, 1, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    n_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    N_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    s_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    S_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    r_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    R_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    h_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    H_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    d_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    D_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    l_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    L_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    u_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    U_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    c_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    C_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    m_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    M_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    f_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    F_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    y_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    Y_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    w_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    W_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    g_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    G_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    p_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    P_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    b_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    B_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    v_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    V_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    k_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    K_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    x_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    X_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    q_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    Q_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    j_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    J_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    z_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    Z_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    dot_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
    space_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]