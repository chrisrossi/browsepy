def register_plugin(manager):
    manager.register_widget(
        place='header',
        type='button',
        endpoint='new_folder',
        text='New Folder',
    )

    manager.register_widget(
        place='entry-actions',
        type='button',
        endpoint='rename',
        text='Rename',
    )
