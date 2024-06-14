from flask_restx import Namespace, Resource, fields

user_ns = Namespace('users', description='User operations')

user_model = user_ns.model('User', {
    'id': fields.String(required=True, description='The user identifier'),
    'email': fields.String(required=True, description='The user email'),
    'first_name': fields.String(required=True, description='The user first name'),
    'last_name': fields.String(required=True, description='The user last name'),
})

# In-memory database simulation
users_db = {}

@user_ns.route('/')
class UserList(Resource):
    @user_ns.doc('list_users')
    @user_ns.marshal_list_with(user_model)
    def get(self):
        '''List all users'''
        return list(users_db.values())

    @user_ns.doc('create_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model, code=201)
    def post(self):
        '''Create a new user'''
        new_user = user_ns.payload
        user_id = str(len(users_db) + 1)
        new_user['id'] = user_id
        users_db[user_id] = new_user
        return new_user, 201

@user_ns.route('/<string:user_id>')
class UserResource(Resource):
    @user_ns.doc('get_user')
    @user_ns.marshal_with(user_model)
    def get(self, user_id):
        '''Fetch a user given its identifier'''
        user = users_db.get(user_id)
        if user is None:
            user_ns.abort(404, "User not found")
        return user

    @user_ns.doc('update_user')
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model)
    def put(self, user_id):
        '''Update a user given its identifier'''
        if user_id not in users_db:
            user_ns.abort(404, "User not found")
        updated_user = user_ns.payload
        updated_user['id'] = user_id
        users_db[user_id] = updated_user
        return updated_user, 200

    @user_ns.doc('delete_user')
    def delete(self, user_id):
        '''Delete a user given its identifier'''
        if user_id in users_db:
            del users_db[user_id]
            return '', 204
        user_ns.abort(404, "User not found")
