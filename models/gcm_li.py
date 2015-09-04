from gcm import GCM


SERVER_API_KEY = "AIzaSyAzMIVFy_Go35pxffRDb8Bei8dP1PcVna0"


def gcm_li(reg_id,reg_data):
    
    gcm = GCM(SERVER_API_KEY)


    reg_list = []
    print "&@#&@&#@#&@#&@&#@#&@&#&#@"
    print reg_id

    reg_list.append(reg_id)

    response_data = reg_data
    response_data['message'] = "you got it"
    #test_reg_data =  {'message': u'APA91bHZ8hH9xv20R-eqwuK9liLVN5cYAPFr9MDFvvCwOBpVv-ygV_NE7T9Dq73pqZiIQBlnyeaENM7Ym3m8Fql-S1VkylqQHzYxUsXEDapxCoDaoOo1mf4s_gBHvyMfrcoYTi0W9RY3', 'queue_num': '1', 'key': '1441338705248', 'doctor': 'adasdasd'}




    
    #data = {'message':'You have x new friends'}

    #reg_id = 'APA91bHDRCRNIGHpOfxivgwQt6ZFK3isuW4aTUOFwMI9qJ6MGDpC3MlOWHtEoe8k6PAKo0H_g2gXhETDO1dDKKxgP5LGulZQxTeNZSwva7tsIL3pvfNksgl0wu1xGbHyQxp2CexeZDKEzvugwyB5hywqvT1-UxxxqpL4EUXTWOm0RXE5CrpMk'

    #gcm.plaintext_request(registration_id=reg_id, data=data)
    response = gcm.json_request(registration_ids=reg_list, data=response_data)



#test_reg_id=['APA91bF6fATDK9bGKRD-wDibpdm7P71N3Adna0A-vTM5zB6dQV9vc49KiepnD0c0vUeSAwoHj0VtSNmNCit6URtWezIubdjUBNbodCx-Z6UTTNcDV_nEYmyxRV0vfPapj4Tu2cTmtl0C']
#test_reg_data = {'queue_num':'5','doctor':'jack'}
#gcm_li(test_reg_id,test_reg_data)

