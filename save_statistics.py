from pathlib import Path 
import os 
import csv 


def check_folder_exists(path):
	if Path(path).is_dir():
		return 
	os.mkdir(path)


def get_plays_csv_structure(playerlog):
	df = {}
	columns = [
		'card_0', 
		'card_1', 
		'card_2', 
		'card_3', 
		'card_4', 
		'card_5', 
		'card_6',
		'qt_civilian_card',
		'qt_military_cards', 
		'qt_commercial_cards',
		'qt_raw_materials',
		'qt_manufactured_good',
		'qt_scientific_cards', 
		'qt_guild_cards', 
		'wonder_id',
		'wonder_stage', 
		'qt_shields',
		'qt_coins',
		'turn',
		'era',
		'action', 
		'time'
	]

	hand = playerlog['hand']
	for idx in range(0, 7):

		if (len(hand) -  1) < idx: 
			card_id = 0
		else: 
			card_id = hand[idx]

		df['card_{}'.format(idx)] = card_id 

	df['action'] = playerlog['action']
	df['qt_civilian_card'] = playerlog['amount']['civilian']
	df['qt_military_cards']	= playerlog['amount']['military']
	df['qt_commercial_cards'] = playerlog['amount']['commercial']
	df['qt_raw_materials'] = playerlog['amount']['raw_material']
	df['qt_manufactured_good'] = playerlog['amount']['manufactured_goods']
	df['qt_scientific_cards'] = playerlog['amount']['scientific']
	df['qt_guild_cards'] = playerlog['amount']['guild']
	df['wonder_id'] = playerlog['wonder_id']
	df['wonder_stage'] = playerlog['wonder_stage']
	df['qt_shields'] = playerlog['resources']['shields']
	df['qt_coins'] = playerlog['resources']['coins']
	df['turn'] = playerlog['turn']
	df['era'] = playerlog['era']
	df['time'] = playerlog['time']
	
	return columns, df   

def save_plays_log(playerlog):
	filename = './historico/dados_jogadas_simple.csv'
	columns, data = get_plays_csv_structure(playerlog)
	check_folder_exists('./historico')
	file_exists = os.path.isfile('./historico/dados_jogadas_simple.csv')

	with open(filename, 'a+') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=columns)
		if not file_exists:
			writer.writeheader()
		writer.writerow(data)


def get_match_csv_structure(playerlog):
	columns = [
		'qt_civilian_card',
		'qt_military_cards', 
		'qt_commercial_cards',
		'qt_raw_materials',
		'qt_manufactured_good',
		'qt_scientific_cards', 
		'qt_guild_cards', 
		'wonder_id',
		'wonder_stage', 
		'qt_clay',
		'qt_coins' ,
		'qt_compass',
		'qt_gear',
		'qt_glass',
		'qt_loom',
		'qt_ore',
		'qt_papyrus',
		'qt_shields',
		'qt_stone',
		'qt_tablet',
		'qt_wood',
		'civilian_points',
		'commercial_points',
		'guild_points',
		'military_points',
		'scientific_points',
		'total_points',
		'wonder_points',
		'winner'
	]

	df = {}
	df['qt_civilian_card'] = playerlog['amount']['civilian']
	df['qt_military_cards']	= playerlog['amount']['military']
	df['qt_commercial_cards'] = playerlog['amount']['commercial']
	df['qt_raw_materials'] = playerlog['amount']['raw_material']
	df['qt_manufactured_good'] = playerlog['amount']['manufactured_goods']
	df['qt_raw_materials'] = playerlog['amount']['raw_material']
	df['qt_scientific_cards'] = playerlog['amount']['scientific']
	df['qt_guild_cards'] = playerlog['amount']['guild']
	df['wonder_id'] = playerlog['wonder_id']
	df['wonder_stage'] = playerlog['wonder_stage']
	df['qt_shields'] = playerlog['resources']['shields']
	df['qt_coins'] = playerlog['resources']['coins']
	df['qt_clay'] = playerlog['resources']['clay']
	df['qt_compass'] = playerlog['resources']['compass']
	df['qt_gear'] = playerlog['resources']['gear']
	df['qt_glass'] = playerlog['resources']['glass']
	df['qt_loom'] = playerlog['resources']['loom']
	df['qt_ore'] = playerlog['resources']['ore']
	df['qt_papyrus'] = playerlog['resources']['papyrus']
	df['qt_stone'] = playerlog['resources']['stone']
	df['qt_tablet'] = playerlog['resources']['tablet']
	df['qt_wood'] = playerlog['resources']['wood']
	df['civilian_points'] = playerlog['points']['civilian']
	df['commercial_points'] = playerlog['points']['commercial']
	df['guild_points'] = playerlog['points']['guild']
	df['military_points'] = playerlog['points']['military']
	df['scientific_points'] = playerlog['points']['scientific']
	df['total_points'] = playerlog['points']['total']
	df['wonder_points'] = playerlog['points']['wonder']
	df['winner'] = playerlog['winner']

	return columns, df 


def save_match_log(playerlog):
	filename = './historico/dados_partidas_simple.csv'
	columns, data = get_match_csv_structure(playerlog)
	file_exists = os.path.isfile('./historico/dados_partidas_simple.csv')
	check_folder_exists('./historico')
	with open(filename, 'a+') as csvfile:
		writer = csv.DictWriter(csvfile, fieldnames=columns)
		if not file_exists:
			writer.writeheader()
		writer.writerow(data)



