import pandas as pd


# # Все тренера и кол-во занятий
# def get_trainers(con):
#     return pd.read_sql('''
#         SELECT idTrainer, fio_tr, COUNT(TrainerRasp.idTrainerRasp)
#         FROM Trainer
#         JOIN TrainerRasp USING(idTrainer)
#         GROUP BY fio_tr''', con)


# Все специальности
def get_spec(con):
    return pd.read_sql('''
        SELECT idTrainerSpec, spec
        FROM TrainerSpec
        GROUP BY idTrainerSpec''', con)