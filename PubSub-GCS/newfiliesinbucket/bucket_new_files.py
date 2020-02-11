def newfilesinbucket(project_id, subscription, path, ack='all'):
    """Return new created files in a path from a bucket
    First create a topic in PubSub
    Second create a subscription from that topic
    Third create notification from a BUCKET to a subscription:
        >gsutil notification create -t $SUBSCRIPTION -f json $BUCKET

    :param project_id: id project
    :param subscription: PubSub subuscription name
    :param path: The path tha you want to verify
    :param ack: all or just_this_folder: acknowledge the message for the bucket modifications
    :return: list of files names

    >>>newfilesinbucket(project_id, subiscription ,path, ack='all')
    ['teste/xxxx.csv', 'teste/wwwww.csv', 'teste/qqqq.py']
    """
    from google.cloud import pubsub_v1
    import re
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(
        project_id, subscription
    )
    path = '^' + path
    if not re.search("/$", path):
        path = path + '/'

    files_list = []

    def callback(message):
        if message.attributes:
            value = message.attributes.get('objectId')
            event = message.attributes.get('eventType') == 'OBJECT_FINALIZE'
            if re.search(path, value) and not(re.search("/$", value)) and event:
                files_list.append(value)
            if ack == 'just_this_folder':
                message.ack()
        if ack == 'all':
            message.ack()

    streaming_pull_future = subscriber.subscribe(
        subscription_path, callback=callback
    )

    try:
        streaming_pull_future.result(timeout=30)
    except:  # noqa
        streaming_pull_future.cancel()
    return list(dict.fromkeys(files_list))
