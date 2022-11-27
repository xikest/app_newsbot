from collections import namedtuple

profile = namedtuple(typename='profiles', field_names=['TOKEN', 'channels'])

class BotProfiles:
        @staticmethod
        def get_botAlert():
            return  profile(TOKEN='5753698180:AAHlOqMGw_Pec-lYW6riVWDsCNiDBaybJ8I',
                            channels={'teat_chat_id' : '-1001673032661',
                                        'nber_chat_id' : '-1001645400224',
                                        'twt_consensus_chat_id' : '-1001686311222',
                                        'twt_chat_id': '-1001609819786',
                                        'teat_w_chat_id' :  '-1001754209136'})
            
        @staticmethod
        def get_botBeta():
            return  profile(TOKEN='5419434216:AAGf88KSC0ETWkSkogbf3N7pmzcQEG0PAQ8',
                            channels={'beta_chat_id' :'-1001601197449'})

        @staticmethod
        def get_botTwitters():
            return  profile(TOKEN='5911658908:AAH_TFHQX5JPZ3GxUDyG6mMIh3IYQMowLkM',
                            
                            channels={'chat_id' :'-1001601197449',
                                'twt_chat_id' :'-1001609819786'})

