# 1단계: 맵 및 프로빈스 구조 생성
class Province:
    def __init__(self, name, coordinates, neighbors=None):
        self.name = name
        self.coordinates = coordinates  # (x, y) 좌표
        self.neighbors = neighbors if neighbors is not None else []

    def add_neighbor(self, neighbor_province):
        self.neighbors.append(neighbor_province)

# 예시로 몇몇 프로빈스 생성
gondor = Province("Gondor", (10, 20))
rohan = Province("Rohan", (15, 25))
mordor = Province("Mordor", (20, 30))

# 인접 프로빈스 설정
gondor.add_neighbor(rohan)
rohan.add_neighbor(gondor)
rohan.add_neighbor(mordor)
mordor.add_neighbor(rohan)

# 프로빈스 출력 확인
for province in [gondor, rohan, mordor]:
    print(f"Province: {province.name}, Coordinates: {province.coordinates}, Neighbors: {[n.name for n in province.neighbors]}")

# 2단계: 자원 관리 시스템 초기 구현

class Province:
    def __init__(self, name, coordinates, resources, neighbors=None):
        self.name = name
        self.coordinates = coordinates  # (x, y) 좌표
        self.resources = resources  # 자원 딕셔너리 {'돈': 0, '식량': 0, '원자재': 0}
        self.neighbors = neighbors if neighbors is not None else []

    def add_neighbor(self, neighbor_province):
        self.neighbors.append(neighbor_province)

    # 자원 생산 함수
    def produce_resources(self):
        for resource, amount in self.resources.items():
            self.resources[resource] += amount  # 매 턴마다 자원을 생산

    # 자원 상태 출력
    def display_resources(self):
        print(f"{self.name} 자원 상태: {self.resources}")

# 예시 프로빈스 생성 (자원: 돈, 식량, 원자재)
gondor = Province("Gondor", (10, 20), {'돈': 5, '식량': 10, '원자재': 7})
rohan = Province("Rohan", (15, 25), {'돈': 3, '식량': 8, '원자재': 6})
mordor = Province("Mordor", (20, 30), {'돈': 6, '식량': 5, '원자재': 9})

# 자원 생산 테스트
for province in [gondor, rohan, mordor]:
    province.produce_resources()  # 자원을 생산
    province.display_resources()  # 자원 상태 출력

# 3단계: 플레이어 클래스와 게임 시작 시스템

class Player:
    def __init__(self, name):
        self.name = name
        self.province = None  # 플레이어가 선택한 프로빈스
        self.resources = {'돈': 0, '식량': 0, '원자재': 0}

    # 플레이어가 프로빈스를 선택
    def choose_province(self, province):
        self.province = province
        self.resources = province.resources.copy()  # 프로빈스 자원을 복사해 플레이어에게 할당

    # 자원 상태 출력
    def display_resources(self):
        print(f"{self.name}의 자원 상태: {self.resources}")

# 예시: 프로빈스 정의
gondor = Province("Gondor", (10, 20), {'돈': 5, '식량': 10, '원자재': 7})
rohan = Province("Rohan", (15, 25), {'돈': 3, '식량': 8, '원자재': 6})
mordor = Province("Mordor", (20, 30), {'돈': 6, '식량': 5, '원자재': 9})

# 플레이어 생성 및 프로빈스 선택
player1 = Player("Player1")
player1.choose_province(gondor)

# 플레이어 자원 상태 출력
player1.display_resources()

# 4단계: 병력 카드 생성 및 배치 시스템

class UnitCard:
    def __init__(self, unit_type, attack, defense, movement):
        self.unit_type = unit_type  # '육군', '해군', '공군'
        self.attack = attack
        self.defense = defense
        self.movement = movement

    def display_unit_info(self):
        print(f"유닛: {self.unit_type}, 공격력: {self.attack}, 방어력: {self.defense}, 이동력: {self.movement}")

# 병력 카드 생성 예시
army = UnitCard('육군', attack=5, defense=8, movement=2)
navy = UnitCard('해군', attack=7, defense=6, movement=3)
airforce = UnitCard('공군', attack=9, defense=4, movement=4)

army.display_unit_info()
navy.display_unit_info()
airforce.display_unit_info()

class Player:
    def __init__(self, name):
        self.name = name
        self.province = None  # 플레이어가 선택한 프로빈스
        self.resources = {'돈': 0, '식량': 0, '원자재': 0}
        self.units = []  # 플레이어가 보유한 병력 카드 리스트

    def choose_province(self, province):
        self.province = province
        self.resources = province.resources.copy()

    def add_unit(self, unit_card):
        self.units.append(unit_card)
    
    def display_units(self):
        print(f"{self.name}의 병력 목록:")
        for unit in self.units:
            unit.display_unit_info()

# 플레이어가 병력을 추가하는 예시
player1 = Player("Player1")
player1.choose_province(gondor)

# 병력 배치
player1.add_unit(army)
player1.add_unit(airforce)

# 플레이어 병력 확인
player1.display_units()

# 5단계: 병력 이동 및 자원 관리 시스템

class Province:
    def __init__(self, name, coordinates, resources, neighbors=None):
        self.name = name
        self.coordinates = coordinates
        self.resources = resources
        self.neighbors = neighbors if neighbors is not None else []

    def add_neighbor(self, neighbor_province):
        self.neighbors.append(neighbor_province)

    # 병력 이동 가능한지 확인
    def can_move_to(self, target_province, movement):
        if target_province in self.neighbors and movement > 0:
            return True
        return False

class Player:
    def __init__(self, name):
        self.name = name
        self.province = None
        self.resources = {'돈': 0, '식량': 0, '원자재': 0}
        self.units = []  # 병력 카드 리스트

    def choose_province(self, province):
        self.province = province
        self.resources = province.resources.copy()

    def add_unit(self, unit_card):
        self.units.append(unit_card)

    def move_unit(self, unit_card, target_province):
        if self.province.can_move_to(target_province, unit_card.movement):
            print(f"{unit_card.unit_type}이(가) {self.province.name}에서 {target_province.name}으로 이동합니다.")
            self.province = target_province
        else:
            print("이동 불가: 너무 멀거나 이동할 수 없는 지역입니다.")

    # 자원 소비 및 관리
    def manage_resources(self):
        for resource, amount in self.resources.items():
            if amount > 0:
                self.resources[resource] -= 1  # 자원 소비 예시
        print(f"{self.name}의 자원 상태: {self.resources}")

# 예시: 프로빈스 설정 및 병력 이동 테스트
gondor = Province("Gondor", (10, 20), {'돈': 5, '식량': 10, '원자재': 7})
rohan = Province("Rohan", (15, 25), {'돈': 3, '식량': 8, '원자재': 6})
gondor.add_neighbor(rohan)

player1 = Player("Player1")
player1.choose_province(gondor)
army = UnitCard('육군', attack=5, defense=8, movement=2)

player1.add_unit(army)
player1.move_unit(army, rohan)  # 병력 이동 시도

# 자원 관리
player1.manage_resources()

import random

# 6단계: 전투 시스템 1차 구현 (주사위 기반)

class UnitCard:
    def __init__(self, unit_type, attack, defense, movement):
        self.unit_type = unit_type
        self.attack = attack
        self.defense = defense
        self.movement = movement

    def display_unit_info(self):
        print(f"유닛: {self.unit_type}, 공격력: {self.attack}, 방어력: {self.defense}, 이동력: {self.movement}")

# 전투 시스템 (주사위 굴림)
def battle(attacker, defender):
    attack_roll = random.randint(1, 6) + attacker.attack
    defense_roll = random.randint(1, 6) + defender.defense

    print(f"{attacker.unit_type} 공격 주사위: {attack_roll}")
    print(f"{defender.unit_type} 방어 주사위: {defense_roll}")

    if attack_roll > defense_roll:
        print(f"{attacker.unit_type}가 {defender.unit_type}을(를) 공격 성공!")
        return "attack_success"
    else:
        print(f"{defender.unit_type}가 {attacker.unit_type}의 공격을 막아냈습니다!")
        return "defense_success"

# 병력 카드 생성 예시
army_attacker = UnitCard('육군', attack=5, defense=8, movement=2)
army_defender = UnitCard('육군', attack=4, defense=6, movement=3)

# 전투 테스트
battle(army_attacker, army_defender)

# 7단계: AI 기초 설정

import random

class AIPlayer(Player):  # Player 클래스를 상속받아 AIPlayer 생성
    def __init__(self, name, personality):
        super().__init__(name)
        self.personality = personality  # 공격적, 수동적, 균형 성향

    # AI 행동 패턴에 따라 병력 배치 및 자원 관리
    def take_turn(self):
        if self.personality == "aggressive":
            print(f"{self.name}은(는) 공격적인 AI입니다!")
            self.manage_resources()
            self.attack_enemy()
        elif self.personality == "passive":
            print(f"{self.name}은(는) 수동적인 AI입니다.")
            self.manage_resources()
            self.defend()
        elif self.personality == "balanced":
            print(f"{self.name}은(는) 균형 잡힌 AI입니다.")
            self.manage_resources()
            if random.choice([True, False]):
                self.attack_enemy()
            else:
                self.defend()

    def attack_enemy(self):
        # 공격 로직 (추후 구현할 수 있음)
        print(f"{self.name}이(가) 공격을 준비합니다!")

    def defend(self):
        # 방어 로직 (추후 구현할 수 있음)
        print(f"{self.name}이(가) 방어 태세를 갖춥니다!")

# AI 플레이어 생성 및 테스트
ai1 = AIPlayer("AI_Player1", "aggressive")
ai2 = AIPlayer("AI_Player2", "passive")
ai3 = AIPlayer("AI_Player3", "balanced")

# AI 행동 테스트
ai1.take_turn()
ai2.take_turn()
ai3.take_turn()

# 8단계: AI 행동 로직 및 턴제 시스템

class TurnSystem:
    def __init__(self, players):
        self.players = players  # 플레이어와 AI 리스트
        self.current_turn = 0

    def next_turn(self):
        player = self.players[self.current_turn]
        print(f"\n--- {player.name}의 턴 ---")
        player.take_turn()  # 각 플레이어가 자신의 턴에 행동함
        self.current_turn = (self.current_turn + 1) % len(self.players)  # 다음 턴으로 전환

class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'돈': 0, '식량': 0, '원자재': 0}

    def take_turn(self):
        print(f"{self.name}의 자원 관리 및 병력 배치")
        self.manage_resources()

    def manage_resources(self):
        print(f"{self.name}이(가) 자원을 관리합니다. (기본 행동)")

class AIPlayer(Player):
    def __init__(self, name, personality):
        super().__init__(name)
        self.personality = personality

    def take_turn(self):
        if self.personality == "aggressive":
            print(f"{self.name}은(는) 공격적인 AI입니다!")
            self.attack_enemy()
        elif self.personality == "passive":
            print(f"{self.name}은(는) 수동적인 AI입니다.")
            self.defend()
        elif self.personality == "balanced":
            print(f"{self.name}은(는) 균형 잡힌 AI입니다.")
            if random.choice([True, False]):
                self.attack_enemy()
            else:
                self.defend()

    def attack_enemy(self):
        print(f"{self.name}이(가) 공격을 준비합니다!")

    def defend(self):
        print(f"{self.name}이(가) 방어 태세를 갖춥니다!")

# 플레이어와 AI 설정
player1 = Player("Player1")
ai1 = AIPlayer("AI_Player1", "aggressive")
ai2 = AIPlayer("AI_Player2", "passive")

# 턴제 시스템 설정
turn_system = TurnSystem([player1, ai1, ai2])

# 턴 진행 테스트
for _ in range(3):  # 3턴 동안 게임 진행
    turn_system.next_turn()

# 9단계: 외교 시스템 구현

class DiplomacySystem:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def propose_alliance(self):
        success = random.randint(1, 100) <= 70  # 70% 확률로 동맹이 성립됨
        if success:
            print(f"{self.player1.name}과 {self.player2.name}이(가) 동맹을 맺었습니다!")
        else:
            print(f"{self.player1.name}의 동맹 제안이 {self.player2.name}에 의해 거절되었습니다.")

    def trade_resources(self, resource, amount):
        if self.player1.resources[resource] >= amount:
            self.player1.resources[resource] -= amount
            self.player2.resources[resource] += amount
            print(f"{self.player1.name}이(가) {self.player2.name}에게 {resource} {amount}만큼을 교환했습니다.")
        else:
            print(f"{self.player1.name}이(가) {resource}가 충분하지 않습니다.")

    def declare_war(self):
        print(f"{self.player1.name}이(가) {self.player2.name}에게 전쟁을 선포했습니다!")
        # 전쟁 로직 추가 예정

# 플레이어 설정
player1 = Player("Player1")
player2 = AIPlayer("AI_Player1", "balanced")

# 외교 시스템 테스트
diplomacy = DiplomacySystem(player1, player2)
diplomacy.propose_alliance()  # 동맹 제안
diplomacy.trade_resources('돈', 5)  # 자원 교환
diplomacy.declare_war()  # 전쟁 선포

# 10단계: UI 및 게임 최종 조정

class GameUI:
    def __init__(self, players):
        self.players = players

    def display_player_info(self, player):
        print(f"\n{player.name}의 정보:")
        print(f"자원 상태: {player.resources}")
        print("보유 병력:")
        for unit in player.units:
            unit.display_unit_info()

    def display_turn_info(self, current_player):
        print(f"\n--- {current_player.name}의 턴 ---")

    def display_diplomacy_options(self, player1, player2):
        print(f"\n{player1.name}은(는) {player2.name}과(와) 외교 활동을 할 수 있습니다:")
        print("1. 동맹 제안")
        print("2. 자원 교환")
        print("3. 전쟁 선포")

# 게임 UI 실행 예시
player1 = Player("Player1")
ai1 = AIPlayer("AI_Player1", "aggressive")

# 자원 설정 (임시 값)
player1.resources = {'돈': 10, '식량': 20, '원자재': 15}
ai1.resources = {'돈': 8, '식량': 18, '원자재': 12}

# 병력 설정 (임시 값)
army = UnitCard('육군', attack=5, defense=8, movement=2)
player1.add_unit(army)
ai1.add_unit(army)

# UI 생성 및 정보 출력
game_ui = GameUI([player1, ai1])
game_ui.display_player_info(player1)
game_ui.display_turn_info(player1)

# 외교 활동 선택
game_ui.display_diplomacy_options(player1, ai1)

# 10단계: UI 및 게임 최종 조정

class GameUI:
    def __init__(self, players):
        self.players = players

    def display_player_info(self, player):
        print(f"\n{player.name}의 정보:")
        print(f"자원 상태: {player.resources}")
        print("보유 병력:")
        for unit in player.units:
            unit.display_unit_info()

    def display_turn_info(self, current_player):
        print(f"\n--- {current_player.name}의 턴 ---")

    def display_diplomacy_options(self, player1, player2):
        print(f"\n{player1.name}은(는) {player2.name}과(와) 외교 활동을 할 수 있습니다:")
        print("1. 동맹 제안")
        print("2. 자원 교환")
        print("3. 전쟁 선포")

# 게임 UI 실행 예시
player1 = Player("Player1")
ai1 = AIPlayer("AI_Player1", "aggressive")

# 자원 설정 (임시 값)
player1.resources = {'돈': 10, '식량': 20, '원자재': 15}
ai1.resources = {'돈': 8, '식량': 18, '원자재': 12}

# 병력 설정 (임시 값)
army = UnitCard('육군', attack=5, defense=8, movement=2)
player1.add_unit(army)
ai1.add_unit(army)

# UI 생성 및 정보 출력
game_ui = GameUI([player1, ai1])
game_ui.display_player_info(player1)
game_ui.display_turn_info(player1)

# 외교 활동 선택
game_ui.display_diplomacy_options(player1, ai1)

# 1단계: 게임 초기화 및 설정 통합

class GameSetup:
    def __init__(self):
        self.players = []  # 플레이어와 AI 리스트
        self.provinces = []  # 프로빈스 리스트

    def initialize_map(self):
        # 프로빈스 생성 및 설정
        gondor = Province("Gondor", (10, 20), {'돈': 5, '식량': 10, '원자재': 7})
        rohan = Province("Rohan", (15, 25), {'돈': 3, '식량': 8, '원자재': 6})
        mordor = Province("Mordor", (20, 30), {'돈': 6, '식량': 5, '원자재': 9})
        gondor.add_neighbor(rohan)
        rohan.add_neighbor(mordor)

        self.provinces.extend([gondor, rohan, mordor])

    def initialize_players(self):
        # 플레이어와 AI 초기화
        player1 = Player("Player1")
        ai1 = AIPlayer("AI_Player1", "aggressive")
        ai2 = AIPlayer("AI_Player2", "passive")

        # 플레이어가 프로빈스 선택
        player1.choose_province(self.provinces[0])
        ai1.choose_province(self.provinces[1])
        ai2.choose_province(self.provinces[2])

        self.players.extend([player1, ai1, ai2])

    def start_game(self):
        print("게임을 시작합니다!")
        self.initialize_map()
        self.initialize_players()

# 게임 시작
game_setup = GameSetup()
game_setup.start_game()

# 2단계: 턴 진행 시스템 구축

class TurnSystem:
    def __init__(self, players):
        self.players = players
        self.current_turn = 0

    def next_turn(self):
        current_player = self.players[self.current_turn]
        print(f"\n--- {current_player.name}의 턴 ---")
        
        # 플레이어가 자원을 관리하거나 병력을 이동하거나 외교를 선택할 수 있음
        current_player.take_turn()
        
        # 다음 플레이어로 턴을 전환
        self.current_turn = (self.current_turn + 1) % len(self.players)
        print(f"다음 플레이어는 {self.players[self.current_turn].name}입니다.\n")

class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'돈': 5, '식량': 10, '원자재': 7}
        self.units = []  # 병력 리스트

    def take_turn(self):
        print(f"{self.name}이(가) 자원 관리 또는 병력 이동을 선택합니다.")
        # 자원 관리, 병력 이동, 외교 중 선택하게 할 수 있음
        self.manage_resources()

    def manage_resources(self):
        print(f"{self.name}이(가) 자원을 관리합니다.")
        for resource, amount in self.resources.items():
            self.resources[resource] += 1  # 예시로 자원을 한 번씩 추가
        print(f"{self.name}의 자원 상태: {self.resources}")

class AIPlayer(Player):
    def __init__(self, name, personality):
        super().__init__(name)
        self.personality = personality

    def take_turn(self):
        print(f"{self.name}의 AI 행동: {self.personality} 전략에 따라 움직임")
        if self.personality == "aggressive":
            self.attack_enemy()
        elif self.personality == "passive":
            self.defend()
        else:
            # 균형 잡힌 성향의 경우 자원 관리와 병력 이동을 무작위로 결정
            if random.choice([True, False]):
                self.attack_enemy()
            else:
                self.defend()

    def attack_enemy(self):
        print(f"{self.name}이(가) 적을 공격합니다!")

    def defend(self):
        print(f"{self.name}이(가) 방어 준비를 합니다.")

# 플레이어와 AI 설정
player1 = Player("Player1")
ai1 = AIPlayer("AI_Player1", "aggressive")
ai2 = AIPlayer("AI_Player2", "passive")

# 턴제 시스템 설정
turn_system = TurnSystem([player1, ai1, ai2])

# 턴 진행 테스트 (예시로 3턴 실행)
for _ in range(3):
    turn_system.next_turn()

# 3단계: 자원 생산 및 소비 관리

class Province:
    def __init__(self, name, coordinates, resources, neighbors=None):
        self.name = name
        self.coordinates = coordinates
        self.resources = resources  # 자원 딕셔너리 {'돈': 0, '식량': 0, '원자재': 0}
        self.neighbors = neighbors if neighbors is not None else []

    def add_neighbor(self, neighbor_province):
        self.neighbors.append(neighbor_province)

    # 자원 생산 함수
    def produce_resources(self):
        for resource, amount in self.resources.items():
            self.resources[resource] += amount  # 매 턴마다 자원을 생산

    # 자원 상태 출력
    def display_resources(self):
        print(f"{self.name} 자원 상태: {self.resources}")

class Player:
    def __init__(self, name):
        self.name = name
        self.province = None  # 플레이어가 선택한 프로빈스
        self.resources = {'돈': 0, '식량': 0, '원자재': 0}
        self.units = []  # 병력 리스트

    def choose_province(self, province):
        self.province = province
        self.resources = province.resources.copy()  # 프로빈스 자원을 플레이어에게 할당

    # 자원 관리: 자원 생산 및 소비
    def manage_resources(self):
        # 자원 생산
        self.province.produce_resources()
        self.resources = self.province.resources.copy()  # 자원 동기화
        print(f"{self.name}의 자원 상태: {self.resources}")

    # 병력 생산 및 자원 소모
    def produce_units(self, unit_type):
        if self.resources['돈'] >= 2 and self.resources['식량'] >= 3:
            new_unit = UnitCard(unit_type, attack=5, defense=5, movement=3)
            self.units.append(new_unit)
            self.resources['돈'] -= 2
            self.resources['식량'] -= 3
            print(f"{self.name}이(가) {unit_type}을(를) 생산했습니다!")
        else:
            print(f"{self.name}의 자원이 부족하여 병력을 생산할 수 없습니다.")

    def display_units(self):
        print(f"{self.name}의 병력 목록:")
        for unit in self.units:
            unit.display_unit_info()

class UnitCard:
    def __init__(self, unit_type, attack, defense, movement):
        self.unit_type = unit_type
        self.attack = attack
        self.defense = defense
        self.movement = movement

    def display_unit_info(self):
        print(f"유닛: {self.unit_type}, 공격력: {self.attack}, 방어력: {self.defense}, 이동력: {self.movement}")

# 예시: 프로빈스 생성 및 자원 생산 테스트
gondor = Province("Gondor", (10, 20), {'돈': 5, '식량': 10, '원자재': 7})
player1 = Player("Player1")
player1.choose_province(gondor)

# 자원 관리 및 병력 생산 테스트
player1.manage_resources()
player1.produce_units('육군')
player1.display_units()

# 4단계: 병력 이동 및 전투 준비

class Province:
    def __init__(self, name, coordinates, resources, neighbors=None):
        self.name = name
        self.coordinates = coordinates
        self.resources = resources  # 자원 딕셔너리 {'돈': 0, '식량': 0, '원자재': 0}
        self.neighbors = neighbors if neighbors is not None else []

    def add_neighbor(self, neighbor_province):
        self.neighbors.append(neighbor_province)

class UnitCard:
    def __init__(self, unit_type, attack, defense, movement):
        self.unit_type = unit_type
        self.attack = attack
        self.defense = defense
        self.movement = movement

    def display_unit_info(self):
        print(f"유닛: {self.unit_type}, 공격력: {self.attack}, 방어력: {self.defense}, 이동력: {self.movement}")

class Player:
    def __init__(self, name):
        self.name = name
        self.province = None  # 플레이어가 선택한 프로빈스
        self.resources = {'돈': 0, '식량': 0, '원자재': 0}
        self.units = []  # 병력 리스트

    def choose_province(self, province):
        self.province = province
        self.resources = province.resources.copy()  # 프로빈스 자원을 플레이어에게 할당

    def add_unit(self, unit_card):
        self.units.append(unit_card)

    # 병력 이동
    def move_unit(self, unit_card, target_province):
        if target_province in self.province.neighbors:
            print(f"{self.name}의 {unit_card.unit_type}이(가) {self.province.name}에서 {target_province.name}으로 이동합니다.")
            self.province = target_province  # 프로빈스 변경
        else:
            print(f"{self.name}의 병력은 {target_province.name}으로 이동할 수 없습니다. (인접하지 않음)")

    # 전투 준비
    def prepare_battle(self, target_province):
        print(f"{self.name}이(가) {target_province.name}에서 전투를 준비 중입니다.")
        # 추가 전투 로직 구현 예정

# 예시: 프로빈스 생성 및 병력 이동 테스트
gondor = Province("Gondor", (10, 20), {'돈': 5, '식량': 10, '원자재': 7})
rohan = Province("Rohan", (15, 25), {'돈': 3, '식량': 8, '원자재': 6})
mordor = Province("Mordor", (20, 30), {'돈': 6, '식량': 5, '원자재': 9})

gondor.add_neighbor(rohan)
rohan.add_neighbor(mordor)

player1 = Player("Player1")
player1.choose_province(gondor)

army = UnitCard('육군', attack=5, defense=8, movement=2)
player1.add_unit(army)

# 병력 이동 및 전투 준비 테스트
player1.move_unit(army, rohan)  # 병력 이동
player1.prepare_battle(rohan)  # 전투 준비

import random

# 5단계: 전투 시스템 확장

class UnitCard:
    def __init__(self, unit_type, attack, defense, movement):
        self.unit_type = unit_type
        self.attack = attack
        self.defense = defense
        self.movement = movement

    def display_unit_info(self):
        print(f"유닛: {self.unit_type}, 공격력: {self.attack}, 방어력: {self.defense}, 이동력: {self.movement}")

# 전투 시스템 (주사위 굴림)
def battle(attacker, defender):
    attack_roll = random.randint(1, 6) + attacker.attack
    defense_roll = random.randint(1, 6) + defender.defense

    print(f"{attacker.unit_type} 공격 주사위: {attack_roll}")
    print(f"{defender.unit_type} 방어 주사위: {defense_roll}")

    if attack_roll > defense_roll:
        print(f"{attacker.unit_type}가 {defender.unit_type}을(를) 공격 성공!")
        return "attack_success"
    else:
        print(f"{defender.unit_type}가 {attacker.unit_type}의 공격을 막아냈습니다!")
        return "defense_success"

# 병력 카드 생성 예시
army_attacker = UnitCard('육군', attack=5, defense=8, movement=2)
army_defender = UnitCard('육군', attack=4, defense=6, movement=3)

# 전투 테스트
battle(army_attacker, army_defender)

import random

# 6단계: 외교 시스템 확장

class DiplomacySystem:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def propose_alliance(self):
        success = random.randint(1, 100) <= 70  # 70% 확률로 동맹이 성립됨
        if success:
            print(f"{self.player1.name}과 {self.player2.name}이(가) 동맹을 맺었습니다!")
        else:
            print(f"{self.player1.name}의 동맹 제안이 {self.player2.name}에 의해 거절되었습니다.")

    def trade_resources(self, resource, amount):
        if self.player1.resources[resource] >= amount:
            self.player1.resources[resource] -= amount
            self.player2.resources[resource] += amount
            print(f"{self.player1.name}이(가) {self.player2.name}에게 {resource} {amount}만큼을 교환했습니다.")
        else:
            print(f"{self.player1.name}이(가) {resource}가 충분하지 않습니다.")

    def declare_war(self):
        print(f"{self.player1.name}이(가) {self.player2.name}에게 전쟁을 선포했습니다!")
        # 전쟁 로직 추가 예정

# 플레이어 및 AI 설정
player1 = Player("Player1")
ai1 = AIPlayer("AI_Player1", "balanced")

# 외교 시스템 테스트
diplomacy = DiplomacySystem(player1, ai1)
diplomacy.propose_alliance()  # 동맹 제안
diplomacy.trade_resources('돈', 5)  # 자원 교환
diplomacy.declare_war()  # 전쟁 선포

# 7단계: AI 전투 및 외교 로직 강화

class AIPlayer(Player):
    def __init__(self, name, personality):
        super().__init__(name)
        self.personality = personality  # 공격적, 수동적, 균형 성향

    def take_turn(self):
        print(f"{self.name}의 AI 행동: {self.personality} 성향에 따라 결정됩니다.")
        
        if self.personality == "aggressive":
            # 공격 성향: 자원을 빠르게 소모하고 병력을 강화
            self.manage_resources()
            self.attack_enemy()
        elif self.personality == "passive":
            # 수동 성향: 자원을 비축하고 방어 위주로 진행
            self.manage_resources()
            self.defend()
        elif self.personality == "balanced":
            # 균형 잡힌 성향: 랜덤하게 공격 또는 방어 결정
            self.manage_resources()
            if random.choice([True, False]):
                self.attack_enemy()
            else:
                self.defend()

    def attack_enemy(self):
        # AI가 상대를 공격할지 결정하는 로직 (전투 준비 상태로 전환)
        print(f"{self.name}이(가) 공격을 준비 중입니다!")
        # 추가 전투 로직은 이후 단계에서 확장 가능

    def defend(self):
        # AI가 방어 태세를 유지하는 로직
        print(f"{self.name}이(가) 방어 전략을 선택했습니다!")

    def consider_diplomacy(self, opponent):
        # AI가 외교 활동을 고려
        if self.personality == "aggressive" and random.randint(1, 100) > 50:
            print(f"{self.name}은(는) 공격적인 성향이므로 동맹을 맺지 않습니다.")
        else:
            print(f"{self.name}이(가) {opponent.name}와 동맹을 맺을 가능성을 고려 중입니다.")
            diplomacy = DiplomacySystem(self, opponent)
            diplomacy.propose_alliance()  # 동맹 시도

# AI 및 플레이어 설정
ai1 = AIPlayer("AI_Player1", "aggressive")
ai2 = AIPlayer("AI_Player2", "balanced")
player1 = Player("Player1")

# AI 외교 및 전투 테스트
ai1.take_turn()
ai2.take_turn()
ai1.consider_diplomacy(player1)  # 외교 시도

# 8단계: 전투 후 자원 및 병력 회복

class UnitCard:
    def __init__(self, unit_type, attack, defense, movement):
        self.unit_type = unit_type
        self.attack = attack
        self.defense = defense
        self.movement = movement

class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'돈': 10, '식량': 20, '원자재': 15}
        self.units = []  # 병력 리스트

    def add_unit(self, unit_card):
        self.units.append(unit_card)

    def display_units(self):
        print(f"{self.name}의 병력 목록:")
        for unit in self.units:
            unit.display_unit_info()

    # 전투 후 자원 보상
    def receive_battle_rewards(self, reward_resources):
        for resource, amount in reward_resources.items():
            self.resources[resource] += amount
        print(f"{self.name}이(가) 전투 보상으로 {reward_resources}을(를) 받았습니다!")

    # 병력 재배치 (전투 후 병력 손실 복구)
    def recover_units(self, unit_type, num_units):
        cost = {'돈': 2, '식량': 3}  # 병력 1개를 복구하는 데 필요한 자원
        if self.resources['돈'] >= cost['돈'] * num_units and self.resources['식량'] >= cost['식량'] * num_units:
            for _ in range(num_units):
                new_unit = UnitCard(unit_type, attack=5, defense=5, movement=3)
                self.add_unit(new_unit)
            self.resources['돈'] -= cost['돈'] * num_units
            self.resources['식량'] -= cost['식량'] * num_units
            print(f"{self.name}이(가) 병력 {num_units}개를 복구했습니다!")
        else:
            print(f"{self.name}이(가) 병력을 복구할 자원이 부족합니다.")

class UnitCard:
    def __init__(self, unit_type, attack, defense, movement):
        self.unit_type = unit_type
        self.attack = attack
        self.defense = defense
        self.movement = movement

    def display_unit_info(self):
        print(f"유닛: {self.unit_type}, 공격력: {self.attack}, 방어력: {self.defense}, 이동력: {self.movement}")

# 전투 후 병력 회복 및 자원 보상 테스트
player1 = Player("Player1")

# 병력 재배치 및 자원 보상 테스트
reward = {'돈': 5, '식량': 10}
player1.receive_battle_rewards(reward)

# 병력 2개 복구 시도
player1.recover_units('육군', 2)
player1.display_units()

# 9단계: 승리 조건 설정

class Game:
    def __init__(self, players, provinces):
        self.players = players
        self.provinces = provinces
        self.game_over = False

    def check_victory(self):
        # 모든 프로빈스를 한 플레이어가 점령하면 승리
        for player in self.players:
            if all(province in player.provinces for province in self.provinces):
                print(f"{player.name}이(가) 모든 프로빈스를 점령했습니다! 게임 종료!")
                self.game_over = True
                return player
        # 자원 목표 달성 시 승리 조건 추가 가능
        for player in self.players:
            if player.resources['돈'] >= 50:
                print(f"{player.name}이(가) 자원 목표를 달성했습니다! 게임 종료!")
                self.game_over = True
                return player

    def check_game_over(self):
        if self.game_over:
            print("게임이 종료되었습니다.")
        else:
            print("게임이 아직 끝나지 않았습니다.")

class Player:
    def __init__(self, name):
        self.name = name
        self.resources = {'돈': 10, '식량': 20, '원자재': 15}
        self.provinces = []

    def add_province(self, province):
        self.provinces.append(province)

    def display_provinces(self):
        print(f"{self.name}이(가) 점령한 프로빈스 목록:")
        for province in self.provinces:
            print(f"- {province.name}")

# 프로빈스 클래스 (기존 코드에서 추가 사용 가능)
class Province:
    def __init__(self, name):
        self.name = name

# 플레이어 및 프로빈스 설정
player1 = Player("Player1")
player2 = Player("Player2")

# 프로빈스 생성 및 할당
gondor = Province("Gondor")
rohan = Province("Rohan")
mordor = Province("Mordor")

player1.add_province(gondor)
player1.add_province(rohan)
player2.add_province(mordor)

# 게임 생성
game = Game([player1, player2], [gondor, rohan, mordor])

# 승리 조건 체크
game.check_victory()
game.check_game_over()
