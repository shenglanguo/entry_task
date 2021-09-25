# NOTE: Generated By HttpRunner v3.1.6
# FROM: testcases/testdemo.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseTestdemo(HttpRunner):

    config = Config("request methods testcase with functions").base_url(
        "http://127.0.0.1:5000"
    )

    teststeps = [
        Step(
            RunRequest("test single match")
            .with_variables(**{"name": "李四"})
            .get("/queryresult")
            .with_params(**{"name": "$name"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.return_info", "success!")
        ),
        Step(
            RunRequest("test two match")
            .with_variables(**{"name": "张"})
            .get("/queryresult")
            .with_params(**{"name": "$name"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.return_info", "success!")
            .assert_equal("body.result[0].name", "张三")
            .assert_equal("body.result[1].name", "张无忌")
        ),
        Step(
            RunRequest("test not supporting request method")
            .with_variables(**{"name": "张"})
            .post("/queryresult")
            .with_params(**{"name": "$name"})
            .validate()
            .assert_equal("body.return_info", "Bad request method!")
            .assert_equal("body.result", False)
            .assert_equal("body.return_code", 404)
        ),
        Step(
            RunRequest("test param is null")
            .get("/queryresult")
            .validate()
            .assert_equal("body.return_info", "Please input word wanted to be query!")
            .assert_equal("body.result", False)
            .assert_equal("body.return_code", 200)
        ),
        Step(
            RunRequest("test english param")
            .with_variables(**{"name": "wangwu"})
            .get("/queryresult")
            .with_params(**{"name": "$name"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.return_info", "success!")
            .assert_equal("body.result[0].name", "$name")
        ),
    ]


if __name__ == "__main__":
    TestCaseTestdemo().test_start()
