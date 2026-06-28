from database.DB_connect import DBConnect
from model.genere import Genere


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getPaesi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select distinct i.BillingCountry as paese
                    from Invoice i 
 """

        cursor.execute(query)

        for row in cursor:
            result.append((row["paese"]))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getNodi(paese):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        res=[]
        query = """
        select distinct g.GenreId ,g.Name 
from Genre g ,Track t ,InvoiceLine il , Invoice i , Customer c 
where g.GenreId = t.GenreId and t.TrackId =il.TrackId and il.InvoiceId = i.InvoiceId and i.CustomerId= c.CustomerId and i.BillingCountry = %s
GROUP BY g.GenreId , g.Name 
having count(t.TrackId )>0
        
        """
        cursor.execute(query, (paese,))

        for row in cursor:
            res.append(Genere(**row))

        cursor.close()
        conn.close()
        return res

