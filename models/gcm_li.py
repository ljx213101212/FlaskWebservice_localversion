from gcm import GCM


SERVER_API_KEY = "AIzaSyAzMIVFy_Go35pxffRDb8Bei8dP1PcVna0"


def gcm_li(reg_id,reg_data):
    
    gcm = GCM(SERVER_API_KEY)


    reg_list = []
    print "&@#&@&#@#&@#&@&#@#&@&#&#@"
    #print reg_id

    reg_list.append(reg_id)

    response_data = reg_data
    print response_data
    #response_data['message'] = "you got it"
    #test_reg_data =  {'message': u'APA91bHZ8hH9xv20R-eqwuK9liLVN5cYAPFr9MDFvvCwOBpVv-ygV_NE7T9Dq73pqZiIQBlnyeaENM7Ym3m8Fql-S1VkylqQHzYxUsXEDapxCoDaoOo1mf4s_gBHvyMfrcoYTi0W9RY3', 'queue_num': '1', 'key': '1441338705248', 'doctor': 'adasdasd'}

    response = gcm.json_request(registration_ids=reg_list, data=response_data)



# test_reg_id=['APA91bH79j8PX1-6642nqkQ54fgM0E1hTVn0wuU3_bSsvC2wY5xlPEUvc0ORH0Lrh0QU4-2u953nB7kWreoowe0cQfnFsbamX8ocHlg8Zs-wOVkFTXS08rMyJADaZ2fC-0a0FfwAbLBxuujeqddDZfN6i5ll3Xk5cg']
# test_reg_data = {'queue_num':'5','doctor':'jack'}
# gcm_li(test_reg_id,test_reg_data)

