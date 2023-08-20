from actions import *


# Creating a dictionary of user actions
directory_actions: dict[str, Action] = {
    "n": NextPageAction("Next page"),
    "p": PreviousPageAction("Previous page"),
    "a": AddRecordAction("Add record"),
    "d": DeleteRecordAction("Delete record"),
    "e": EditRecordAction("Edit record"),
    "f": SearchRecordsAction("Search for record"),
    "s": SaveChangesAction("Save changes"),
    "x": QuitAction("Quit"),
    "q": QuitWithoutSavingAction("Quit without saving"),
}

# Creating a legend to display available actions
directory_actions_legend = (
    "".join(
        [
            f"{action.name} '{action_key}', "
            for action_key, action in directory_actions.items()
        ]
    )
)[:-2]
