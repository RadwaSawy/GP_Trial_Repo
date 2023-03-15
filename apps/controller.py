from models import *


class controller:
    def addUser(email, password, name):
        newUser = Users(email=email, password=password, name=name)
        db.session.add(newUser)
        db.session.commit()

    def editUser(id, email='', password='', name=''):
        user = Users.query.filter_by(id=id).first()
        if email != '':
            user.email = email
        if password != '':
            user.password = password
        if name != '':
            user.name = name
        db.session.commit()

    def deleteUser(id):
        user = Users.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()

    def addUserLocation(name, user_id):
        newUserLocation = UserLocations(name=name, user_id=user_id)
        db.session.add(newUserLocation)
        db.session.commit()

    def editUserLocation(id, user_id=0, name=''):
        userLocation = UserLocations.query.filter_by(id=id).first()
        if user_id != 0:
            userLocation.user_id = user_id
        if name != '':
            userLocation.name = name
        db.session.commit()

    def deleteUserLocation(id):
        userLocation = UserLocations.query.filter_by(id=id).first()
        db.session.delete(userLocation)
        db.session.commit()

    def addUserMember(name, user_id, location_id=0):
        newUserMember = UserMembers(
            name=name, user_id=user_id, location_id=location_id)
        db.session.add(newUserMember)
        db.session.commit()

    def editUserMember(id, user_id=0, name='', location_id=0):
        userMember = UserMembers.query.filter_by(id=id).first()
        if user_id != 0:
            userMember.user_id = user_id
        if name != '':
            userMember.name = name
        if location_id != 0:
            userMember.location_id = location_id
        db.session.commit()

    def deleteUserMember(id):
        userMember = UserMembers.query.filter_by(id=id).first()
        db.session.delete(userMember)
        db.session.commit()

    def addMedia(url, type, user_id, location_id=0, member_id=0):
        newMedia = Media(url=url, user_id=user_id, type=type,
                         location_id=location_id, member_id=member_id)
        db.session.add(newMedia)
        db.session.commit()

    def editMedia(id, url='', type='', user_id=0, location_id=0, member_id=0):
        media = Media.query.filter_by(id=id).first()
        if user_id != 0:
            media.user_id = user_id
        if url != '':
            media.url = url
        if location_id != 0:
            media.location_id = location_id
        if member_id != 0:
            media.member_id = member_id
        if type != '':
            media.type = type
        db.session.commit()

    def deleteMedia(id):
        media = Media.query.filter_by(id=id).first()
        db.session.delete(media)
        db.session.commit()

    def addAnalysisResult(media_id, result=''):
        newAnalysisResult = AnalysisResults(media_id=media_id, result=result)
        db.session.add(newAnalysisResult)
        db.session.commit()

    def editAnalysisResult(id, media_id=0, result=''):
        analysisResult = AnalysisResults.query.filter_by(id=id).first()
        if media_id != 0:
            analysisResult.media_id = media_id
        if result != '':
            analysisResult.result = result
        db.session.commit()

    def deleteAnalysisResult(id):
        analysisResult = AnalysisResults.query.filter_by(id=id).first()
        db.session.delete(analysisResult)
        db.session.commit()
