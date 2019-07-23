def zero_reset(m_n_matrix):

    if not m_n_matrix:
        raise Exception('m_n_matrix cannot be of NoneType')


    m_size = len(m_n_matrix)#tracks number of rows we have
    n_size = len(m_n_matrix[0])#tracks number of columns we have


    for x in range(n_size):#for each column
        for y in range(m_size):#and for each row

            if m_n_matrix[y][x] == 0 :#if zero set column, row to zero, if not m_n_matrix[x][y] == 0
                set_row_zero(y, n_size, m_n_matrix)
                set_column_zero(m_size, x, m_n_matrix)

    return s1

def set_row_zero(row, column_size, m_n_matrix):
    for x in range(column_size):
        m_n_matrix[row][x] = 0

def set_column_zero(row_size, column, m_n_matrix):
    for x in range(row_size):
        m_n_matrix[x][column] = 0

s1 = [[1,2],[3,4],[5,6],[7,8]]
print(zero_reset(s1))
