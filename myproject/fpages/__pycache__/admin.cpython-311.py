�
    �Gd�  �                   �   � d dl mZ d dlmZ d dlmZ d dlmZ  G d� de�  �        Zej	        �
                    e�  �         ej	        �                    ee�  �         dS )�    )�admin)�FlatPageAdmin)�FlatPage)�gettext_lazyc                   �:   � e Zd Zdddif ed�  �        ddd�ffZdS )r   N�fields)�url�title�content�siteszAdvanced options)�collapse)�enable_comments�registration_required�template_name)�classesr   )�__name__�
__module__�__qualname__�_�	fieldsets� �    �B   D:\Учеба\module-D1.5_Project_Django\myproject\fpages\admin.pyr   r      sH   � � � � � �	��>�?�@�	
���	�	�$��!
� !
� 	�
�I�I�Ir   r   N)�django.contribr   �django.contrib.flatpages.adminr   �django.contrib.flatpages.modelsr   �django.utils.translationr   r   �site�
unregister�registerr   r   r   �<module>r!      s�   ��  �  �  �  �  �  � 8� 8� 8� 8� 8� 8� 4� 4� 4� 4� 4� 4� 6� 6� 6� 6� 6� 6�� � � � �M� � � � �
� � �h� � � � �
� � �H�m� ,� ,� ,� ,� ,r   