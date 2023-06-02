import pandas as pd
import bd

    def toxlsx:
        bda = bd.bd()
        d = bda.listatudo()
        df = pd.DataFrame(d, columns=["marca", "modelo", "valor"])
        df.to_excel('celulares.xlsx', index=False, header=True)
