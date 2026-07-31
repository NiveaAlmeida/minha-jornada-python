{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP8yy2BtTtpCZfszOK9ZFDr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/NiveaAlmeida/minha-jornada-python/blob/main/02-estruturas-dados/dicionarios.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "5S9S2-XqXZyc",
        "outputId": "07e54403-506e-4f0c-a4cd-1dd7abaa9d6c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number between 1 and 12: 1\n",
            "January\n"
          ]
        }
      ],
      "source": [
        "#Beecrowd 1052\n",
        "meses = {\n",
        "    1: 'January',\n",
        "    2: 'February',\n",
        "    3: 'March',\n",
        "    4: 'April',\n",
        "    5: 'May',\n",
        "    6: 'June',\n",
        "    7: 'July',\n",
        "    8: 'August',\n",
        "    9: 'September',\n",
        "    10: 'October',\n",
        "    11: 'November',\n",
        "    12: 'December'\n",
        "    }\n",
        "mes = input('Enter a number between 1 and 12: ')\n",
        "mes = int(mes)\n",
        "print(meses[mes])"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Beecrowd 2850\n",
        "\n",
        "condicoes = {\n",
        "    'esquerda': 'ingles',\n",
        "    'direita': 'frances',\n",
        "    'nenhuma': 'portugues',\n",
        "    'ambas': 'caiu'\n",
        "}\n",
        "condicao = input('Digite a condição: ').strip().lower()\n",
        "print(condicoes[condicao])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "rzmSz96RaBaR",
        "outputId": "1c52de24-91db-428b-c60c-58e5e4f52c6e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a condição: esquerda\n",
            "ingles\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Beecrowd 1281\n",
        "N = int(input())\n",
        "for _ in range(N): # Iterate N times for N test cases\n",
        "  M = int(input())\n",
        "  produto_preco = {}\n",
        "  for m in range(M):\n",
        "    produto, preco_str = input(\"Digite o produto e seu preço (ex: Maçã: 2.90): \").lower().split(\": \")\n",
        "    produto_preco[produto] = float(preco_str) # Convert price to float\n",
        "\n",
        "  P = int(input())\n",
        "  current_case_total = 0.0 # Initialize total for the current test case\n",
        "  for p in range (P):\n",
        "    produto_a_comprar, qtd_str = input().lower().split(\": \")\n",
        "    qtd = int(qtd_str) # Convert quantity to int\n",
        "\n",
        "    if produto_a_comprar in produto_preco:\n",
        "      current_case_total += produto_preco[produto_a_comprar] * qtd\n",
        "  print(f\"R$ {current_case_total:.2f}\") # Print total for each test case, formatted to 2 decimal places.\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 263
        },
        "id": "86Qi6dqIaMSA",
        "outputId": "22a4affc-3bf2-48d9-af52-b197ed496699"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "1\n",
            "2\n",
            "Digite o produto e seu preço (Mação: 2.90, p2: p2): Maçã: 2.90, Uva: 4.50\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "AttributeError",
          "evalue": "'list' object has no attribute 'split'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_30995/4113678702.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      5\u001b[0m   \u001b[0mproduto_preco\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m   \u001b[0;32mfor\u001b[0m \u001b[0mm\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mM\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 7\u001b[0;31m     \u001b[0mproduto\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mpreco_str\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Digite o produto e seu preço (Mação: 2.90, p2: p2): \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\": \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msplit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\", \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      8\u001b[0m     \u001b[0mproduto_preco\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mproduto\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mfloat\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpreco_str\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;31m# Convert price to float\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      9\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mAttributeError\u001b[0m: 'list' object has no attribute 'split'"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# -*- coding: utf-8 -*-\n",
        "\n",
        "N = int(input())  # número de idas à feira\n",
        "\n",
        "for _ in range(N):\n",
        "    M = int(input())  # quantidade de produtos disponíveis\n",
        "    produtos = {}\n",
        "\n",
        "    # lê os M produtos e seus preços\n",
        "    for _ in range(M):\n",
        "        nome, preco = input().split()\n",
        "        produtos[nome] = float(preco)\n",
        "\n",
        "    P = int(input())  # quantidade de produtos que Dona Parcinova quer comprar\n",
        "    total = 0.0\n",
        "\n",
        "    # lê a lista de compras e calcula o valor\n",
        "    for _ in range(P):\n",
        "        nome, qtd = input().split()\n",
        "        qtd = int(qtd)\n",
        "        total += produtos[nome] * qtd\n",
        "\n",
        "    # imprime o resultado formatado\n",
        "    print(f\"R$ {total:.2f}\")\n"
      ],
      "metadata": {
        "id": "G3-khZY5huHL"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Beecrowd 1281\n",
        "N = int(input(\"Quantidade de idas à feira: \"))\n",
        "\n",
        "for _ in range(N): # Iterate N times for N test cases\n",
        "  M = int(input(\"Quantidade de produtos: \"))\n",
        "  produto_preco = {}\n",
        "  for m in range(M):\n",
        "    produto, preco_s = input(\"Digite o produto e seu preço (produto: preço): \").lower().split(\": \")\n",
        "    produto_preco[produto] = float(preco_s)\n",
        "\n",
        "  P = int(input(\"Quantos produtos a serem comprados? \"))\n",
        "  total = 0.0 # Initialize total for the current test case\n",
        "  for p in range (P):\n",
        "    produto_a_comprar, qtd_s = input(\"Digite o produto a ser comprado e a quantidade (Produto: quantidade): \").lower().split(\": \")\n",
        "    qtd = int(qtd_s)\n",
        "\n",
        "    if produto_a_comprar in produto_preco:\n",
        "      total += produto_preco[produto_a_comprar] * qtd\n",
        "  print(f\"R$ {total:.2f}\") # Print total for each test case, formatted to 2 decimal places.\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 582
        },
        "id": "d7BgD742g3aA",
        "outputId": "b33ab205-b106-4dc8-e45b-ec908a9d15ac"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Quantidade de idas à feira: 2\n",
            "Quantidade de produtos: 6\n",
            "Digite o produto e seu preço (produto: preço): Maçã: 3.00\n",
            "Digite o produto e seu preço (produto: preço): Pêra: 4.50\n",
            "Digite o produto e seu preço (produto: preço): Laranja: 1.00\n",
            "Digite o produto e seu preço (produto: preço): Manga: 4.50\n",
            "Digite o produto e seu preço (produto: preço): Chuchu: 7.00\n",
            "Digite o produto e seu preço (produto: preço): Jiló: 3.00\n",
            "Quantos produtos a serem comprados? 3\n",
            "Digite o produto a ser comprado e a quantidade (Produto: quantidade): Jiló: 2\n",
            "Digite o produto a ser comprado e a quantidade (Produto: quantidade): Maçã: 8\n",
            "Digite o produto a ser comprado e a quantidade (Produto: quantidade): Manga: 10\n",
            "R$ 75.00\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_42504/585117081.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      4\u001b[0m \u001b[0;32mfor\u001b[0m \u001b[0m_\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mN\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m \u001b[0;31m# Iterate N times for N test cases\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 5\u001b[0;31m   \u001b[0mM\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Quantidade de produtos: \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      6\u001b[0m   \u001b[0mproduto_preco\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m{\u001b[0m\u001b[0;34m}\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      7\u001b[0m   \u001b[0;32mfor\u001b[0m \u001b[0mm\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mrange\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mM\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m   1175\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1176\u001b[0m             )\n\u001b[0;32m-> 1177\u001b[0;31m         return self._input_request(\n\u001b[0m\u001b[1;32m   1178\u001b[0m             \u001b[0mstr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mprompt\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1179\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0;34m\"shell\"\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.12/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m   1217\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1218\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1219\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1220\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1221\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Beecrowd 1281\n",
        "N = int(input(\"Quantidade de idas à feira\"))\n",
        "\n",
        "for _ in range(N): # Iterate N times for N test cases\n",
        "  M = int(input(\"Quantidade de produtos: \"))\n",
        "  produto_preco = {}\n",
        "  for m in range(M):\n",
        "    produto, preco_str = input(\"Digite o produto e seu preço (produto: preço): \").lower().split(\": \")\n",
        "    produto_preco[produto] = float(preco_str)\n",
        "\n",
        "  P = int(input(\"Quantos produtos a serem comprados? \"))\n",
        "  current_case_total = 0.0 # Initialize total for the current test case\n",
        "  for p in range (P):\n",
        "    produto_a_comprar, qtd_str = input(\"Digite o produto a ser comprado e a quantidade (Produto: quantidade): \").lower().split(\": \")\n",
        "    qtd = int(qtd_str)\n",
        "\n",
        "    if produto_a_comprar in produto_preco:\n",
        "      current_case_total += produto_preco[produto_a_comprar] * qtd\n",
        "  print(f\"R$ {current_case_total:.2f}\") # Print total for each test case, formatted to 2 decimal places.\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 349
        },
        "outputId": "14709b2b-c563-4ec2-ef7d-332f68a2702e",
        "id": "prOYcc-QkYmr"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Quantidade de idas à feira2\n",
            "Quantidade de produtos: 3\n",
            "Digite o produto e seu preço (produto: preço): Maçã: 2.90\n",
            "Digite o produto e seu preço (produto: preço): Uva: 3.50\n",
            "Digite o produto e seu preço (produto: preço): Pêra: 2.00\n",
            "Quantos produtos a serem comprados? 2\n",
            "Digite o produto a ser comprado e a quantidade (Produto: quantidade): Maçã: 2\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "TypeError",
          "evalue": "'float' object does not support item assignment",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
            "\u001b[0;32m/tmp/ipykernel_42504/3720681961.py\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     19\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mproduto_a_comprar\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mproduto_preco\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     20\u001b[0m       \u001b[0;32mif\u001b[0m \u001b[0mproduto_a_comprar\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mproduto_comprado\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 21\u001b[0;31m         \u001b[0mtotal\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mproduto_comprado\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mproduto_a_comprar\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m]\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mproduto_preco\u001b[0m\u001b[0;34m[\u001b[0m\u001b[0mproduto_a_comprar\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0mqtd\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     22\u001b[0m   \u001b[0mi\u001b[0m \u001b[0;34m+=\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     23\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtotal\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mTypeError\u001b[0m: 'float' object does not support item assignment"
          ]
        }
      ]
    }
  ]
}