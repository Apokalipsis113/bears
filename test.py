from bears import Bears
import pytest
import json


def tearDown():
    """Allow cear server after avery test"""
    Bears().delete_all_bears()


def test_info():
    res = Bears().get_info()['code']
    assert res == 200


def test_add_and_del():
    res = Bears().post_bear_create("BROWN", "KEKA4", 50)
    # decode index from adding method to delete bear
    del_res = Bears().delete_bear(id=int(res['text']))['code']
    assert res['code'] == 200 and del_res == 200

# not effective but works with unittest as test method of TestCase if needed


def test_add_good_boring():
    # adding bears with allowed formats
    good1 = Bears().post_bear_create("BROWN", "One", 1)["code"]
    good2 = Bears().post_bear_create("POLAR", "Two", 2)["code"]
    good3 = Bears().post_bear_create("BLACK", "Three", 3)["code"]
    good4 = Bears().post_bear_create("GUMMY", "Four", 4)["code"]
    # get result text
    res = Bears().get_all_bears()['text']

    # if bears added text become bigger that 2, and every responce code must be 200
    assert len(
        res) > 2 and good1 == 200 and good2 == 200 and good3 == 200 and good4 == 200

# creating big number of allowed variations


@pytest.mark.parametrize("type", ["BROWN", "POLAR", "BLACK", "GUMMY"])
@pytest.mark.parametrize("name", ["One", "Two", "three", "Four"])
@pytest.mark.parametrize("age", [1, 2, 3, 4])
def test_add_good(type, name, age):
    # adding bears with allowed formats
    assert 200 == Bears().post_bear_create("BROWN", "One", 1)["code"]

# not effective but works with unittest as test method of TestCase if needed


def test_add_bad_boring():
    # expect rised exeption trying add bears with not allowed format
    with pytest.raises(json.JSONDecodeError):
        Bears().post_bear_create("FAKE", "Five", 5)
        Bears().post_bear_create("GUMMY", "Six", -1)
        Bears().post_bear_create("GUMMY", 8, 8)
        Bears().post_bear_create(9, "Nine", 9)
    res = Bears().get_all_bears()['text']
    # check responce size to make sure nothing was added
    assert len(res) == 2

# creating big number of not allowed variations


@pytest.mark.parametrize("type", ["Pinky", 123, "_BLACK_", "  "])
@pytest.mark.parametrize("name", [123, "five", "Six", "Seven"])
@pytest.mark.parametrize("age", [0, -1, 3000000])
def test_add_bad(type, name, age):
    # expect rised exeption trying add bears with not allowed format
    with pytest.raises(json.JSONDecodeError):
        Bears().post_bear_create(type, name, age)


def test_add_check_delete():
    Bears().delete_all_bears()
    # add bear
    add_res = int(Bears().post_bear_create("BROWN", "KEKA4", 50)['text'])
    # getting bear by id
    check_res = Bears().get_bear(id=add_res)['json']
    # deleting bear by id
    del_res = Bears().delete_bear(id=add_res)['code']
    # check that added bear is correctm and delete responce code was 200
    assert {"bear_type": "BROWN", "bear_name": "KEKA4",
            "bear_age": 50, "bear_id": add_res} == check_res, del_res == 200


def test_del_all():
    # check responce code fore delete request
    assert Bears().delete_all_bears()['code'] == 200
