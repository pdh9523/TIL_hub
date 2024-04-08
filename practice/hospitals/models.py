from django.db import models

# Create your models here.
class Doctor(models.Model):
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'
    
class Patient(models.Model):
    # 여기 쓴다고 해서 Patient 모델의 직접적인 변화가 생기는 것이 아니다.
    # 새로운 ManyToManyField를 만들어 관리하게된다.
    # 어느 모델에 적용해도 상관없으나
    # 참조 / 역참조 관계에 대해서 잘 생각해야한다.
    # 이 문장을 가지고 있는 경우 속성값이 존재하는 것 -> 참조
    # 이 문장을 가지고 있지 않은 경우 속성값이 없음 -> 역참조
    # patient1.doctor.add(doctor1)
    # doctor1.patient_set.add(patient1)
    doctors = models.ManyToManyField(Doctor, through='Reservation', related_name='patients')     
    name = models.TextField()

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'
    

class Reservation(models.Model):

    doctors = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    symptom = models.TextField()
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.doctors.pk}번 의사의 {self.patient.pk}번 환자' 