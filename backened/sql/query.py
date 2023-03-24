


CONST_SELECT_ALL_QUERY = "SELECT user_name, email_address, dob, uid FROM user"

CONST_INSERT = "INSERT INTO user (user_name, password, email_address, dob, address, uid ) VALUES(:user_name , :password, :email_address, :dob, :address, :uid)"

CONST_LOGIN = "SELECT id, user_name, password, email_address, dob, uid FROM user WHERE (user_name = :user_name)"

CONST_PROFILE = "SELECT * FROM user WHERE uid = :uid"