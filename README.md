# pydev
Python/Django/Apache2 Sandbox built with Ansible.


VM Notes

- pydev/share is shared with /vagrant_data in the VM
- You need to update your hosts file with: 192.168.33.51 pydev.local
- mysql user/pass: pyguy/pypass
- Django project is installed outside of Apache web root in /vagrant_data/pyproj
- website points to /vagrant_data/pydev.local
- pydev.sql is imported with some sample data for the Django app