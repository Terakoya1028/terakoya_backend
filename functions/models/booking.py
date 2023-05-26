import hashlib
import os
import sys
from enum import Enum
from typing import List, Any, Dict, Union
from pydantic import BaseModel, EmailStr

ROOT_DIR_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(ROOT_DIR_PATH)

from utils.dt import DT

# Define a private member with '__' prefix
# https://rinatz.github.io/python-book/ch03-02-scopes/

# Difference between private and protected member
# https://www.nblog09.com/w/2019/01/09/python-protected-private/


class TERAKOYA_TYPE(Enum):
    """テラコヤ種別 (terakoya_type)"""
    HIGH_IKE = 1
    """カフェ塾テラコヤ(池袋)"""
    ONLINE_TAMA = 2
    """オンラインテラコヤ(多摩)"""
    MID_IKE = 3
    """テラコヤ中等部(池袋)"""
    MID_SHIBU = 4
    """テラコヤ中等部(渋谷)"""


class ARRIVAL_TIME(Enum):
    """到着予定時間帯 (arrival_time)"""
    BEFORE_1700 = 1
    """17:00前"""
    BETWEEN_1700_1730 = 2
    """17:00~17:30"""
    BETWEEN_1730_1800 = 3
    """17:30~18:00"""
    AFTER_1800 = 4
    """18:00以降"""


class GRADE(Enum):
    """学年 (grade)"""
    HIGH_SCHOOL_1 = 1
    """高校1年生"""
    HIGH_SCHOOL_2 = 2
    """高校2年生"""
    HIGH_SCHOOL_3 = 3
    """高校3年生"""
    JUNIOR_HIGH_SCHOOL_1 = 11
    """中学1年生"""
    JUNIOR_HIGH_SCHOOL_2 = 12
    """中学2年生"""
    JUNIOR_HIGH_SCHOOL_3 = 13
    """中学3年生"""
    OTHER = 0
    """その他"""


class TERAKOYA_EXPERIENCE(Enum):
    """テラコヤ経験 (terakoya_experience)"""
    FIRST_TIME = 1
    """今回が初回"""
    DONE = 2
    """過去に参加したことがある"""


class STUDY_SUBJECT(Enum):
    """勉強したい科目 (study_subject)"""
    ENGLISH = 1
    """英語"""
    JAPANESE = 2
    """国語"""
    MATH = 3
    """数学"""
    SOCIAL_STUDIES = 4
    """社会"""
    SCIENCE = 5
    """理科"""
    AO_ENTRANCE = 6
    """推薦型入試対策（志望理由書・面接など）"""
    ORIENTATION = 7
    """大学説明会"""
    CAREER = 8
    """キャリア説明会"""
    EIKEN = 9
    """英検"""
    OTHER = 0
    """その他"""


class STUDY_STYLE(Enum):
    """勉強スタイル (study_style)"""
    SILENT = 1
    """黙々と静かに勉強したい"""
    ASK = 2
    """分からない点があったらスタッフに質問したい"""
    TALKING = 3
    """友達と話しながら楽しく勉強したい"""
    WITH = 4
    """1人では難しいのでスタッフ付きっ切りで勉強を教えて欲しい"""
    CONSULT = 5
    """勉強も教えて欲しいけどスタッフの話を聞いたり、相談したい"""
    OTHER = 0
    """その他"""
    NULL = -1
    """未選択"""


class COURSE_CHOICE(Enum):
    """文理選択 (course_choice)"""
    TBD = 1
    """まだ決めていない"""
    LIBERAL_ARTS = 2
    """文系"""
    SCIENCE = 3
    """理系"""
    OTHER = 0
    """その他"""
    NULL = -1
    """未選択"""


class HOW_TO_KNOW_TERAKOYA(Enum):
    """テラコヤを知ったきっかけ (how_to_know_terakoya)"""
    HP = 1
    """HP"""
    INSTAGRAM = 2
    """Instagram"""
    FACEBOOK = 3
    """Facebook"""
    TWITTER = 4
    """Twitter"""
    INTRODUCE = 5
    """知人の紹介"""
    POSTER = 6
    """ポスター・ビラ"""
    OTHER = 0
    """その他"""
    NULL = -1
    """未選択"""


class __CommonProperties(BaseModel):
    name: str
    # Check whether the email format is valid based on RFC 5322 using EmailStr type
    # https://qiita.com/koralle/items/93b094ddb6d3af917702#emailstr
    # https://docs.pydantic.dev/latest/usage/types/#pydantic-types
    # https://qiita.com/yoshitake_1201/items/40268332cd23f67c504c
    email: EmailStr
    # Validation based on Enum
    # https://qiita.com/sand/items/ca2c7c49e8bd94053b04
    terakoya_type: TERAKOYA_TYPE
    arrival_time: ARRIVAL_TIME
    grade: GRADE
    terakoya_experience: TERAKOYA_EXPERIENCE
    study_subject: STUDY_SUBJECT
    study_subject_detail: str
    study_style: STUDY_STYLE
    school_name: str
    first_choice_school: str
    course_choice: COURSE_CHOICE
    future_free: str
    like_thing_free: str
    how_to_know_terakoya: HOW_TO_KNOW_TERAKOYA
    remarks: str


class BookRequestBody(__CommonProperties):
    """
    Request body sent via API Gateway
    """
    attendance_date_list: List[str]


class PLACE(Enum):
    """拠点 (Place)"""
    TBD = 0
    """未設定"""
    SUNSHINE = 1
    """サンシャインシティ"""
    RYOHIN = 2
    """良品計画本社"""
    DIORAMA_CAFE = 3
    """DIORAMA CAFE"""
    CAREER_MOM = 4
    """キャリア・マム"""
    KIKAGAKU = 5
    """キカガク"""
    NULL = -1
    """NULL"""


TERAKOYA_TYPE_TO_PLACE_MAP: Dict[TERAKOYA_TYPE, PLACE] = {
    TERAKOYA_TYPE.HIGH_IKE: PLACE.TBD,  # カフェ塾テラコヤ(池袋) -> TBD
    TERAKOYA_TYPE.ONLINE_TAMA: PLACE.CAREER_MOM,  # オンラインテラコヤ(多摩) -> キャリア・マム
    TERAKOYA_TYPE.MID_IKE: PLACE.SUNSHINE,  # テラコヤ中等部(池袋) -> サンシャインシティ
    TERAKOYA_TYPE.MID_SHIBU: PLACE.KIKAGAKU,  # テラコヤ中等部(渋谷) -> キカガク
}


class REMIND_STATUS(Enum):
    """リマインド状況 (is_reminded)"""
    NOT_SENT = 0
    """未送信"""
    SENT = 1
    """送信済み"""


class BookingItem(__CommonProperties):
    """
    Item that is converted from a request body sent via API Gateway and then to be inserted into DynamoDB  
    """
    date: str
    sk: str = ""
    place: PLACE = PLACE.NULL
    is_reminded: REMIND_STATUS = REMIND_STATUS.NOT_SENT
    timestamp: int = int(DT.CURRENT_JST_DATETIME.timestamp())
    timestamp_iso: str = DT.CURRENT_JST_DATETIME.strftime("%Y-%m-%d %H:%M:%S")
    date_unix_time: int = -1
    uid: str = ""

    # kwargs is a dictionary of arguments. args is a tuple of positional arguments.
    # https://note.nkmk.me/python-args-kwargs-usage/
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.place = TERAKOYA_TYPE_TO_PLACE_MAP[self.terakoya_type]
        self.sk = f"#{self.email}#{self.terakoya_type.value}"
        self.date_unix_time = DT.convert_iso_to_timestamp(self.date)
        self.uid = hashlib.md5(f"#{self.date}{self.sk}".encode()).hexdigest()

    def to_dict(self) -> Dict[str, Union[str, int, float, bool]]:
        """Convert the instance to a dictionary, replacing Enum members with their values."""
        return {k: v.value if isinstance(v, Enum) else v for k, v in self.__dict__.items()}
