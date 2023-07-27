from celery import shared_task


def call_extra_service(loan_dni):
    pass


@shared_task
def extra_functions(loan_dni):
    call_extra_service(loan_dni)
