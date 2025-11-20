"use client";
import { useState, useEffect } from "react";
import { useParams } from "next/navigation";
import useSWR from "swr";
import MainLayout from "@/components/layout/MainLayout";
import Image from "next/image";
import { pontoTuristicoService } from "@/services/pontoTuristicoService";
import { avaliacaoService } from "@/services/avaliacaoService";
import Avaliacao from "@/components/ponto-turistico/Avaliacao";
import FormularioAvaliacao from "@/components/pontoturistico/FormularioAvaliacao";
import useAuthStore from "@/store/authStore";
import BotaoFavorito from "@/components/ponto-turistico/BotaoFavorito";

const fetchPonto = (id) => pontoTuristicoService.getById(id);
const fetchAvaliacoes = (id) => avaliacaoService.getByPonto(id);

export default function DetalhesPontoPage() {
  const params = useParams();
  const { id } = params;
  const { isAuthenticated } = useAuthStore();

  const { data: ponto, error: errorPonto } = useSWR(id, fetchPonto);
  const {
    data: avaliacoes,
    error: errorAvaliacoes,
    mutate,
  } = useSWR(id, fetchAvaliacoes);

  const handleAvaliacaoCriada = (novaAvaliacao) => {
    mutate([novaAvaliacao, ...avaliacoes], false);
  };

  if (errorPonto || errorAvaliacoes) return <div>Falha ao carregar</div>;
  if (!ponto || !avaliacoes) return <div>Carregando...</div>;

  return (
    <MainLayout>
      <div className="container mx-auto px-4 py-12">
        {/* Imagem do ponto */}
        <div className="relative h-96 w-full mb-8">
          <Image
            src={ponto.imagem_url || "/placeholder.jpg"}
            alt={ponto.nome}
            layout="fill"
            objectFit="cover"
            className="rounded-lg"
          />
        </div>

        {/* Título com botão de favorito */}
        <div className="flex items-center justify-between mb-4">
          <h1 className="text-4xl font-display font-bold">{ponto.nome}</h1>
          {isAuthenticated && <BotaoFavorito pontoId={ponto.id} />}
        </div>

        {/* Descrição */}
        <p className="text-lg text-gray-700 mb-8">{ponto.descricao}</p>

        {/* Seção de avaliações */}
        <div className="mt-12">
          <h2 className="text-3xl font-bold mb-6">Avaliações</h2>

          {isAuthenticated && (
            <FormularioAvaliacao
              pontoId={ponto.id}
              onAvaliacaoCriada={handleAvaliacaoCriada}
            />
          )}

          <div className="mt-8">
            {avaliacoes.map((avaliacao) => (
              <Avaliacao key={avaliacao.id} avaliacao={avaliacao} />
            ))}
          </div>
        </div>
      </div>
    </MainLayout>
  );
}
