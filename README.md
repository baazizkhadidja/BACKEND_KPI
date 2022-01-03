# BACKEND_KPI

For the Backend

## 1/ install and create virtual env:

install pip: sudo apt-get install python3-pip
sudo pip3 install virtualenv 
create a virtual environment: virtualenv venv 

## 2/cd to the directory where requirements.txt is located.

## 3/activate your virtualenv . ./env/bin/activate

## 4/run: pip install -r requirements.txt in your shell.

## 5/Run './manage runserver' for a dev server. 

## 6/ Get APIs: 

* List all the investments, by navigate to:
 http://127.0.0.1:8000/api/investissements/ 

 * List investments filtered by ville , by navigate to:
 http://127.0.0.1:8000/investissement_filter/ville-/

 * List investments filtered by etat_d_avancement , by navigate to:
 http://127.0.0.1:8000/investissement_filter/-etat_d_avancement/

  * List investments filtered by ville and/or by etat_d_avancement
, by navigate to:
 http://127.0.0.1:8000/investissement_filter/ville-etat_d_avancement/

 * Get a single investment by id, by navigate to:
 http://127.0.0.1:8000/api/investissement/id 
