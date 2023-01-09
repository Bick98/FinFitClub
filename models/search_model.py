import pandas as pd


# Все тренера и кол-во занятий
def get_trainers(con):
    return pd.read_sql('''
        SELECT idTrainer, fio_tr, COUNT(TrainerRasp.idTrainerRasp)
        FROM Trainer
        JOIN TrainerRasp USING(idTrainer)
        GROUP BY fio_tr''', con)


# Все специальности
def get_spec(con):
    return pd.read_sql('''
        SELECT idTrainerSpec, spec, COUNT(Trainer.idTrainer)
        FROM TrainerSpec
        JOIN Trainer USING(idTrainerSpec)
        GROUP BY spec''', con)


def convert(list):
    # Converting integer list to string list
    s = [str(i) for i in list]

    # Join list items using join()
    res = ",".join(s)

    return res


# def card(con, spec_tr, tr):
#     spec_tr = convert(spec_tr)
#     tr = convert(tr)
#     return pd.read_sql(f'''
#
#     WITH get_spec(idTrainerSpec, spec) AS (SELECT idTrainerSpec,spec
#      FROM Trainer
#      JOIN TrainerSpec USING (idTrainerSpec)
#      GROUP BY idTrainerSpec)
#         SELECT
#         	fio_tr AS 'ФИО тренера',
#         	spec AS 'Cпециализация',
#         	price AS 'Стоимость тренировки',
#             data_tr AS 'Дата тренировки',
#             nach_tr AS 'Начало тренировки',
#             idTrainerRasp AS 'ID'
#         FROM TrainerRasp
#         JOIN Trainer USING(idTrainer)
#         JOIN get_spec USING(idTrainerSpec)
#         GROUP BY idTrainerRasp
#         HAVING (idTrainer IN ({tr}) OR ({not tr}))
#             AND (idTrainerSpec IN ({spec_tr}) OR ({not spec_tr}))
#         ORDER BY
#             fio_tr,
#             spec,
#             price DESC,
#             data_tr DESC
#     ''', con)


# def card(con, tr):
#     tr = convert(tr)
#     return pd.read_sql(f'''
#         SELECT
#         	fio_tr AS 'ФИО_тренера',
#         	price AS 'Стоимость_тренировки',
#             data_tr AS 'Дата_тренировки',
#             nach_tr AS 'Начало_тренировки',
#             idTrainerRasp AS 'ID'
#         FROM TrainerRasp
#         JOIN Trainer USING(idTrainer)
#         GROUP BY idTrainerRasp
#         HAVING (idTrainer IN ({tr}) OR ({not tr}))
#         ORDER BY
#             fio_tr,
#             price DESC,
#             data_tr DESC
#     ''', con)

def card(con, spec_tr, tr):
    spec_tr = convert(spec_tr)
    tr = convert(tr)
    return pd.read_sql(f'''

    WITH get_trainer(idTrainerRasp,idTrainer, fio_trainer, tr_spec, tr_price, idTrainerSpec) AS (

    WITH get_spec(idTrainerSpec, spec) AS (SELECT idTrainerSpec,spec
     FROM Trainer
     JOIN TrainerSpec USING (idTrainerSpec)
     GROUP BY idTrainerSpec)

    SELECT idTrainerRasp,idTrainer, fio_tr, spec, price, idTrainerSpec
     FROM TrainerRasp 
     JOIN Trainer USING (idTrainer)
     JOIN get_spec USING (idTrainerSpec)
     GROUP BY idTrainerRasp)
        SELECT
        	fio_trainer AS 'ФИО тренера',
        	tr_spec AS 'Cпециализация',
        	tr_price AS 'Стоимость тренировки',
            pos_data AS 'Дата тренировки',
            pos_time AS 'Начало тренировки',
            oplata AS 'Оплата',
            idPoseshenie AS 'ID'
        FROM Poseshenie
        JOIN get_trainer t USING(idTrainerRasp)
        GROUP BY idPoseshenie
        HAVING (idTrainer IN ({tr}) OR ({not tr}))
            AND (idTrainerSpec IN ({spec_tr}) OR ({not spec_tr}))
        ORDER BY
            fio_trainer,
            tr_spec,
            tr_price DESC,
            pos_data DESC
    ''', con)