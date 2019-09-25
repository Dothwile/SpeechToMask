import Main
import RPIO.GPIO as GPIO
import GPIOHandler


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
        RPIO.output(self.pin, self.e_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_E(self):
        RPIO.output(self.pin, self.E_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_t(self):
        RPIO.output(self.pin, self.t_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_T(self):
        RPIO.output(self.pin, self.T_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_a(self):
        RPIO.output(self.pin, self.a_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_A(self):
        RPIO.output(self.pin, self.A_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_o(self):
        RPIO.output(self.pin, self.o_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_O(self):
        RPIO.output(self.pin, self.O_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_i(self):
        RPIO.output(self.pin, self.i_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_I(self):
        RPIO.output(self.pin, self.I_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_n(self):
        RPIO.output(self.pin, self.n_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_N(self):
        RPIO.output(self.pin, self.N_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_s(self):
        RPIO.output(self.pin, self.s_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_S(self):
        RPIO.output(self.pin, self.S_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_r(self):
        RPIO.output(self.pin, self.r_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_R(self):
        RPIO.output(self.pin, self.R_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_h(self):
        RPIO.output(self.pin, self.h_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_H(self):
        RPIO.output(self.pin, self.H_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_d(self):
        RPIO.output(self.pin, self.d_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_D(self):
        RPIO.output(self.pin, self.D_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_l(self):
        RPIO.output(self.pin, self.l_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_L(self):
        RPIO.output(self.pin, self.L_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_u(self):
        RPIO.output(self.pin, self.u_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_U(self):
        RPIO.output(self.pin, self.U_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_c(self):
        RPIO.output(self.pin, self.c_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_C(self):
        RPIO.output(self.pin, self.C_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_m(self):
        RPIO.output(self.pin, self.m_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_M(self):
        RPIO.output(self.pin, self.M_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_f(self):
        RPIO.output(self.pin, self.f_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_F(self):
        RPIO.output(self.pin, self.F_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_y(self):
        RPIO.output(self.pin, self.y_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_Y(self):
        RPIO.output(self.pin, self.Y_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_w(self):
        RPIO.output(self.pin, self.w_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_W(self):
        RPIO.output(self.pin, self.W_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_g(self):
        RPIO.output(self.pin, self.g_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_G(self):
        RPIO.output(self.pin, self.G_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_p(self):
        RPIO.output(self.pin, self.p_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_P(self):
        RPIO.output(self.pin, self.P_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_b(self):
        RPIO.output(self.pin, self.b_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_B(self):
        RPIO.output(self.pin, self.B_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_v(self):
        RPIO.output(self.pin, self.v_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_V(self):
        RPIO.output(self.pin, self.V_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_k(self):
        RPIO.output(self.pin, self.k_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_K(self):
        RPIO.output(self.pin, self.K_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_x(self):
        RPIO.output(self.pin, self.x_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_X(self):
        RPIO.output(self.pin, self.X_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_q(self):
        RPIO.output(self.pin, self.q_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_Q(self):
        RPIO.output(self.pin, self.Q_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_j(self):
        RPIO.output(self.pin, self.j_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_J(self):
        RPIO.output(self.pin, self.J_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_z(self):
        RPIO.output(self.pin, self.z_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_Z(self):
        RPIO.output(self.pin, self.Z_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

    def shift_out_dot(self):
        RPIO.output(self.pin, self.dot_map[GPIOHandler.cur_col()][GPIOHandler.get_row()])

    def shift_out_space(self):
        RPIO.output(self.pin, self.space_map[GPIOHandler.get_col()][GPIOHandler.get_row()])

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
    # Inverted each sequence 8 long, only last 5 bits row encoding
    # first 3 tied to column, should be common on list columns
    # rotate 90 counter-clockwise from last bit in each column to get
    # bit map of letter displayed (ignore first 3)
    e_map = [[0, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 1, 0, 1, 1, 0]]  #
    E_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 0, 1]]  #
    t_map = [[0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0, 1, 0]]  #
    T_map = [[0, 0, 1, 0, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 1]]  #
    a_map = [[0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1, 1, 0]]  #
    A_map = [[0, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0]]  #
    o_map = [[0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0, 1, 0], [1, 0, 0, 0, 1, 1, 0, 0]]  #
    O_map = [[0, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0]]  #
    i_map = [[0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 0]]  #
    I_map = [[0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 0, 0, 0]]  #
    n_map = [[0, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1, 0, 0]]  #
    N_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0]]  #
    s_map = [[0, 0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 1, 0, 1, 0]]  #
    S_map = [[0, 0, 1, 1, 0, 0, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 0, 1]]  #
    r_map = [[0, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 1, 0, 0]]  #
    R_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 0, 1, 1, 0, 1, 0]]  #
    h_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0, 0, 0]]  #
    H_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 1, 1, 1]]  #
    d_map = [[0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 1, 1, 1, 1]]  #
    D_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 1, 1, 0]]  #
    l_map = [[0, 0, 1, 1, 0, 0, 0, 1], [0, 1, 0, 1, 1, 1, 1, 1], [1, 0, 0, 1, 0, 0, 0, 0]]  #
    L_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 0, 0, 0, 0]]  #
    u_map = [[0, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 1, 1, 1, 1, 0]]  #
    U_map = [[0, 0, 1, 0, 1, 1, 1, 1], [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1]]  #
    c_map = [[0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 0, 0, 1, 0], [1, 0, 0, 1, 0, 0, 1, 0]]  #
    C_map = [[0, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0]]  #
    m_map = [[0, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1, 1, 0]]  #
    M_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 1, 0], [1, 0, 0, 1, 1, 1, 1, 1]]  #
    f_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1]]  #
    F_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 0, 1]]  #
    y_map = [[0, 0, 1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1]]  #
    Y_map = [[0, 0, 1, 0, 0, 0, 1, 1], [0, 1, 0, 1, 1, 1, 0, 0], [1, 0, 0, 0, 0, 0, 1, 1]]  #
    w_map = [[0, 0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 1, 1, 0, 0]]  #
    W_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1, 0, 0], [1, 0, 0, 1, 1, 1, 1, 1]]  #
    g_map = [[0, 0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 1, 0, 1, 1, 0], [1, 0, 0, 0, 1, 1, 1, 0]]  #
    G_map = [[0, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 1, 1, 1, 0, 1]]  #
    p_map = [[0, 0, 1, 1, 1, 1, 0, 0], [0, 1, 0, 0, 1, 0, 1, 0], [1, 0, 0, 0, 0, 1, 0, 0]]  #
    P_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 0]]  #
    b_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0]]  #
    B_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1, 0]]  #
    v_map = [[0, 0, 1, 0, 1, 1, 0, 0], [0, 1, 0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 0]]  #
    V_map = [[0, 0, 1, 0, 0, 1, 1, 1], [0, 1, 0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 0, 1, 1, 1]]  #
    k_map = [[0, 0, 1, 1, 1, 1, 1, 0], [0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0, 0]]  #
    K_map = [[0, 0, 1, 1, 1, 1, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1]]  #
    x_map = [[0, 0, 1, 1, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 0], [1, 0, 0, 1, 0, 1, 0, 0]]  #
    X_map = [[0, 0, 1, 1, 1, 0, 1, 1], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 1, 1, 0, 1, 1]]  #
    q_map = [[0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 1, 0], [1, 0, 0, 1, 1, 1, 0, 0]]  #
    Q_map = [[0, 0, 1, 0, 1, 1, 1, 0], [0, 1, 0, 1, 1, 0, 0, 1], [1, 0, 0, 1, 1, 1, 1, 0]]  #
    j_map = [[0, 0, 1, 1, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0, 1]]  #
    J_map = [[0, 0, 1, 0, 1, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 1, 1, 1, 1]]  #
    z_map = [[0, 0, 1, 1, 1, 0, 1, 0], [0, 1, 0, 1, 1, 1, 1, 0], [1, 0, 0, 1, 0, 1, 1, 0]]  #
    Z_map = [[0, 0, 1, 1, 1, 0, 0, 1], [0, 1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 1, 0, 0, 1, 1]]  #
    dot_map = [[0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]  #
    space_map = [[0, 0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]]  #