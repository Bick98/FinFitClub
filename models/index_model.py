import pandas as pd

def get_client(con):
    return pd.read_sql(
        '''SELECT idClients, fio FROM Clients
''', con)


def get_trainer_for_client(con, idClients):
    # выбираем и выводим записи о том, какие тренировки были у клиента
    return pd.read_sql('''

    WITH get_trainer(idTrainerRasp, fio_trainer, tr_spec, price) AS (

    WITH get_spec(idTrainerSpec, spec) AS (SELECT idTrainerSpec,spec
     FROM Trainer
     JOIN TrainerSpec USING (idTrainerSpec)
     GROUP BY idTrainerSpec)

    SELECT idTrainerRasp,fio_tr, spec, price
     FROM TrainerRasp 
     JOIN Trainer USING (idTrainer)
     JOIN get_spec USING (idTrainerSpec)
     GROUP BY idTrainerRasp)


SELECT fio_trainer AS 'ФИО тренера',
        tr_spec AS Cпециализация,
       pos_data  AS 'Дата тренировки',
       pos_time  AS 'Время тренировки',
       price AS Стоимость,
       oplata AS Оплата,
       idPoseshenie
FROM Clients       
         JOIN Poseshenie USING (idClients)
         JOIN get_trainer USING (idTrainerRasp)
WHERE Clients.idClients = :id
ORDER BY 3
         ''', con, params={"id": idClients})

# для обработки данных о новом клиенте
def get_new_client(con, new_fio, new_age, new_gender, new_pass):
    cur = con.cursor()

    cur.execute('''
INSERT INTO Clients(fio, age, gender, pass) VALUES (:new_fio, :new_age, :new_gender, :new_pass)
    ''', {"new_fio": new_fio,"new_age": new_age, "new_gender": new_gender, "new_pass": new_pass})

    con.commit()

    return cur.lastrowid

# для обработки данных о новой записи в посещения
def zapis_na_trenirovku(con, idClients,idPoseshenie):
    cur = con.cursor()

    cur.executescript(f'''
UPDATE Poseshenie
SET idClients ={idClients}
WHERE idPoseshenie = {idPoseshenie}
    ''')
    return con.commit()

# для обработки данных об оплате
def pay_tr(con, idPoseshenie):
    cur = con.cursor()

    cur.executescript(f'''
    UPDATE Poseshenie
    SET oplata = true
    WHERE idPoseshenie = {idPoseshenie} 
        ''')
    return con.commit()




