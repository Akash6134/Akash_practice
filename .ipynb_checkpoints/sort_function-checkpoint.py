{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "15e7413e",
   "metadata": {},
   "outputs": [],
   "source": [
    "def my_sorting(lisst):\n",
    "    for i in range(0,len(lisst)):\n",
    "        for j in range(i+1,len(lisst)):\n",
    "            if lisst[i]>lisst[j]:\n",
    "                temp = lisst[i]\n",
    "                lisst[i] = lisst[j]\n",
    "                lisst[j] = temp\n",
    "    return lisst"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25d83abe",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
