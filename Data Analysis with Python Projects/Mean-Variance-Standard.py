import numpy as np

def calculate(list):
    try:
        if len(list) == 9:
            t = np.array(list, dtype=int).reshape(3, 3)
            resultados = {
                'mean': [t.mean(axis=0), t.mean(axis=1), t.mean()],
                'variance': [t.var(axis=0), t.var(axis=1), t.var()],
                'standard deviation': [t.std(axis=0), t.std(axis=1), t.std()],
                'max': [t.max(axis=0), t.max(axis=1), t.max()],
                'min': [t.min(axis=0), t.min(axis=1), t.min()],
                'sum': [t.sum(axis=0), t.sum(axis=1), t.sum()]
            }

            for contas in resultados:
                g = resultados[contas]
                t = [[x for x in g[0]], [x for x in g[1]], g[2]]
                resultados[contas] = t
            return resultados

        else:
            raise ValueError("List must contain nine numbers.")


    except ValueError:
        raise



if __name__ == '__main__':
    print(calculate([0,1,2,3,4,5,6,7,8]))
#LINK DE TESTE:https://replit.com/@LuizSinx/boilerplate-mean-variance-standard-deviation-calculator-2#mean_var_std.py