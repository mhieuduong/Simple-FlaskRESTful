Dự án xây dựng REST API với Flask-RESTful
Có các API trong hệ thống:

    GET  /items              lấy về các item trong hệ thống
    GET  /item/<string:name> lấy về thông tin của item
    POST /item/<string:name> tạo mới thông tin item
    PUT  /item/<string:name> tạo hoặc cập nhật thông tin của item  
    DEL  /item/<string:name> xóa item 
    
    GET  /stores              lấy thông tin của tất cả các store
    GET  /store/<string:name> lấy về thông tin của store
    POST /store/<string:name> tạo mới thông tin store 
    PUT  /store/<string:name> tạo hoặc cập nhật thông tin của store
    DEL  /store/<string:name> xóa store

    POST /register            tạo mới nick tại hệ thống
    POST /auth                lấy token khi đã đăng nhập

Các API yêu cầu token được khởi tạo từ /auth. Token được tạo từ JWT

Cấu trúc thư mục

    __models : chứa các phương thức giao tiếp với CSDL
    __resources : chứa các phương thức cho các lớp item, store,..
    __templates : chứa tệp .html
    __log       : chứa log file
    app.py      : khởi tạo chương trình
    security.py : chứa phương thức xác thực và định danh

Chương trình được chạy trên raspberry pi 4.
Chương trình có thể truy cập tại địa chỉ http://restapitest.webhop.me:8080/



