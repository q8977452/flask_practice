def abort_msg(e):
    error_class = e.__class__.__name__  # 引發錯誤的 class
    detail = e.args[0]  # 得到詳細的訊息

    # generate the error message
    errMsg = {error_class: [detail]}
    return errMsg