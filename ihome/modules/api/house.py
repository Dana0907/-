import datetime

from flask import current_app, jsonify, request, g, session,render_template
from ihome import sr, db
from ihome.models import Area, House, Facility, HouseImage, Order, User
from ihome.modules.api import api_blu
from ihome.utils import constants
from ihome.utils.common import login_required
from ihome.utils.constants import AREA_INFO_REDIS_EXPIRES, QINIU_DOMIN_PREFIX, HOUSE_LIST_PAGE_CAPACITY, \
    HOME_PAGE_MAX_HOUSES, HOME_PAGE_DATA_REDIS_EXPIRES
from ihome.utils.image_storage import storage_image
from ihome.utils.response_code import RET


# 我的发布列表
@api_blu.route('/user/houses')
@login_required
def get_user_house_list():
    pass
    """
    获取用户房屋列表
    1. 获取当前登录用户id
    2. 查询数据
    :return:
     """
    user_id = g.user_id
    if not user_id:
        return jsonify(errno=RET.USERERR, errmsg="请先登录")

    try:
        user = User.query.get(user_id)

    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno = RET.DATAERR, errmsg = "数据库数据出错")

    user_house = user.houses
    house_list = user_house
    house_dict = []
    for house1 in house_list if house_list else None:
        house_dict.append(house1.to_basic_dict())





    return jsonify(errno = RET.OK, errmsg = "OK", data = house_dict)
# 获取地区信息
@api_blu.route("/areas")
def get_areas():
    """
    1. 查询出所有的城区
    2. 返回
    :return:
    """
    try:
        area_list = Area.query.all()
    except Exception as e:
        current_app.logger.error(e)
        return jsonify(errno=RET.DATAERR, errmsg="数据库查询数据出错")
    area_dict = []
    for area in area_list if area_list else None:
        area_dict.append(area.to_dict())

    return jsonify(errno=RET.OK, errmsg="OK", data= area_dict)
# 上传房屋图片
@api_blu.route("/houses/<int:house_id>/images", methods=['POST'])
@login_required
def upload_house_image(house_id):
    """
    1. 取到上传的图片
    2. 进行七牛云上传
    3. 将上传返回的图片地址存储
    4. 进行返回
    :return:
    """

# 发布房源
@api_blu.route("/houses", methods=["GET","POST"])
@login_required
def save_new_house():
    """
    1. 接收参数并且判空

    2. 将参数的数据保存到新创建house模型
    3. 保存house模型到数据库
    前端发送过来的json数据
    {
        "title":"",
        "price":"",
        "area_id":"1",
        "address":"",
        "room_count":"",
        "acreage":"",
        "unit":"",
        "capacity":"",
        "beds":"",
        "deposit":"",
        "min_days":"",
        "max_days":"",
        "facility":["7","8"]
    }
    :return:
    """

# 房屋详情
@api_blu.route('/houses/<int:house_id>')
def get_house_detail(house_id):
    """
    1. 通过房屋id查询出房屋模型
    :param house_id:
    :return:
    """
    pass


# 获取首页展示内容
@api_blu.route('/houses/index')
def house_index():
    """
    获取首页房屋列表
    :return:
    """
    pass


# 搜索房屋/获取房屋列表
@api_blu.route('/houses')
def get_house_list():
    pass
